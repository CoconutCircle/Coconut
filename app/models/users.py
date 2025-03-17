
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr
import uuid
from app.schemas.types import FriendshipStatus




# User Model with UUID
class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    name: str = Field(..., min_length=3, max_length=255, regex=r"^[a-zA-Z\s]+$")
    email: EmailStr = Field(..., unique=True)
    profile_pic: Optional[str] = Field(default=None)



class Friends(SQLModel, table=True):
    friendship_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    user_id_1: uuid.UUID = Field(..., foreign_key="user.id")
    user_id_2: uuid.UUID = Field(..., foreign_key="user.id")
    status: FriendshipStatus = Field(...)

    