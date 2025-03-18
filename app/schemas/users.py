from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models.users import User


class Token(BaseModel):
    id_token:str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
class UserBase(BaseModel):
    name: str
    email: EmailStr
    created_at: datetime
    profile_pic: str
