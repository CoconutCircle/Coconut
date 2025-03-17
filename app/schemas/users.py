from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models import User
from enum import Enum

class Token(BaseModel):
    id_token:str

class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    USER = "user"
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role : UserRoleEnum = UserRoleEnum.USER
