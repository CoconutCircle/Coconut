from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 


class Token(BaseModel):
    id_token:str

class UserCreate(BaseModel):
    name: str
    email: str
    profile_picture: Optional[str] = None


class UserRead(BaseModel):
    user_id: str
    name: str
    email: str
    profile_picture: Optional[str] = None
    created_at: datetime



