from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, date
from typing import Optional, List, TYPE_CHECKING
from app.models.modelutils import TimestampMixin
from app.schemas.types import TripStatus, InviteStatus, MemberRole
from app.models.base import generate_trip_id, generate_invite_id,generate_trip_member_id

if TYPE_CHECKING:
    from app.models.users import User, UserTrip
    from app.models.tripdetails import Expense, Media, Itinerary
    from app.models.tripcomms import Chat


class Trip(TimestampMixin, SQLModel, table=True):
    __tablename__ = "trips"
    
    trip_id: Optional[str] = Field(
        default_factory=generate_trip_id, primary_key=True, index=True
    )
    trip_name: str
    created_by: str = Field(foreign_key="users.user_id")
    start_date: date
    end_date: date
    location: str
    is_public: bool = False
    trip_status: TripStatus = Field(default=TripStatus.INCOMING)
    


class TripInvite(TimestampMixin, SQLModel, table=True):
    __tablename__ = "trip_invites"
    
    invite_id: Optional[str] = Field(
        default_factory=generate_invite_id, primary_key=True, index=True
    )
    trip_id: str = Field(foreign_key="trips.trip_id")
    sender_id: str = Field(foreign_key="users.user_id")
    receiver_id: str = Field(foreign_key="users.user_id")
    invite_link: str = Field(unique=True, index=True)
    status: InviteStatus = Field(default=InviteStatus.PENDING)
    
class TripMember(SQLModel, table=True):
    __tablename__ = "trip_members"
    
    member_id: Optional[str] = Field(
        default_factory=generate_trip_member_id, primary_key=True, index=True
    )
    trip_id: str = Field(foreign_key="trips.trip_id")  
    user_id: str = Field(foreign_key="users.user_id")
    role: MemberRole = Field(default=MemberRole.MEMBER)
    joined_at: datetime = Field(default_factory=datetime.now)
