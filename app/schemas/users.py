from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models.users import User
from app.models.trips import Trip


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

class UserComplete(BaseModel):
    user: User
    trips: list[Trip]
    friends: list
    invites: list
    expenses: list
    media: list
class Token(BaseModel):
    id_token: str


