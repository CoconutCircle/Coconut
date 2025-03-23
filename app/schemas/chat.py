from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from app.models.users import User
from app.schemas.types import TripStatus, InviteStatus, MediaType
from datetime import date


class ChatCreate(BaseModel):
    trip_id: str
    sender_id: str
    message: str


class ChatRead(BaseModel):
    message_id: str
    trip_id: str
    user_id: str
    message: str
    timestamp: datetime
