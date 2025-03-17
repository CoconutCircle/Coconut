
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional
from pydantic import EmailStr
import enum
import uuid

# Enum for User Roles
class UserRoleEnum(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"

# User Model with UUID
class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    name: str = Field(..., min_length=3, max_length=255, regex=r"^[a-zA-Z\s]+$")
    email: EmailStr = Field(..., unique=True)
    role: UserRoleEnum = Field(default=UserRoleEnum.USER)