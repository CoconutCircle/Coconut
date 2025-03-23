from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from app.models.modelutils import TimestampMixin
from app.schemas.types import FriendshipStatus, TripStatus
from app.models.base import generate_user_id, generate_friendship_id, generate_usertrip_id

if TYPE_CHECKING:
    from app.models.tripdetails import Expense, Media
    from app.models.trips import Trip, TripInvite
    from app.models.tripcomms import Chat


class User(TimestampMixin, SQLModel, table=True):
    __tablename__ = "users"

    user_id: Optional[str] = Field(
        default_factory=generate_user_id, primary_key=True, index=True
    )
    name: str
    email: str = Field(unique=True, index=True)
    profile_picture: Optional[str] = None

    # Remove complex relationships for now
    # We'll add only simple ones


class Friendship(TimestampMixin, SQLModel, table=True):
    __tablename__ = "friends"

    friendship_id: Optional[str] = Field(
        default_factory=generate_friendship_id, primary_key=True, index=True
    )
    user_id_1: str = Field(foreign_key="users.user_id")
    user_id_2: str = Field(foreign_key="users.user_id")
    status: FriendshipStatus = Field(default=FriendshipStatus.PENDING)


class UserTrip(SQLModel, table=True):
    __tablename__ = "user_trips"

    record_id: Optional[str] = Field(
        default_factory=generate_usertrip_id, primary_key=True, index=True
    )
    user_id: str = Field(foreign_key="users.user_id")
    trip_id: str = Field(foreign_key="trips.trip_id")
    trip_status: TripStatus