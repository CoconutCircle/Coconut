from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models.users import User
from app.schemas.types import TripStatus, InviteStatus, MediaType
from datetime import date


class MediaCreate(BaseModel):
    trip_id: str
    media_url: str
    media_type: MediaType


class MediaRead(BaseModel):
    media_id: str
    trip_id: str
    user_id: str
    media_url: str
    media_type: MediaType
    uploaded_at: datetime
