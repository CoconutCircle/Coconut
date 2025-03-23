
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models.users import User
from app.schemas.types import TripStatus, InviteStatus, MediaType
from datetime import date



class ItineraryCreate(BaseModel):
    trip_id: str
    title: str
    description: Optional[str] = None
    date: date
    time: Optional[str] = None


class ItineraryRead(BaseModel):
    itinerary_id: str
    trip_id: str
    title: str
    description: Optional[str] = None
    date: date
    time: Optional[str] = None
    created_at: datetime
