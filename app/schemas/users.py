from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 


from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    profile_picture: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[str] = None


class Token(BaseModel):
    id_token: str


