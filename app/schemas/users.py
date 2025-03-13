from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models import User

class Token(BaseModel):
    id_token:str
    
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    
