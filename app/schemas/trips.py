
from pydantic import BaseModel
from app.schemas.types import TripStatus, InviteStatus
from datetime import date, datetime

class TripCreate(BaseModel):
    trip_name: str
    start_date: date
    end_date: date
    location: str
    is_public: bool = False


class TripInviteCreate(BaseModel):
    trip_id: str
    receiver_id: str


class TripInviteRead(BaseModel):
    invite_id: str
    trip_id: str
    sender_id: str
    receiver_id: str
    invite_link: str
    status: InviteStatus
    created_at: datetime
