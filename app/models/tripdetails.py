from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, date
from typing import Optional, List, TYPE_CHECKING
from app.models.modelutils import TimestampMixin
from app.schemas.types import MediaType
from app.models.base import generate_itinerary_id, generate_expense_id, generate_media_id

if TYPE_CHECKING:
    from app.models.trips import Trip
    from app.models.users import User


class Itinerary(TimestampMixin, SQLModel, table=True):
    __tablename__ = "itineraries"

    itinerary_id: Optional[str] = Field(
        default_factory=generate_itinerary_id, primary_key=True, index=True
    )
    trip_id: str = Field(foreign_key="trips.trip_id")
    title: str
    description: Optional[str] = None
    date: date
    time: Optional[str] = None


class Expense(TimestampMixin, SQLModel, table=True):
    __tablename__ = "expenses"

    expense_id: Optional[str] = Field(
        default_factory=generate_expense_id, primary_key=True, index=True
    )
    trip_id: str = Field(foreign_key="trips.trip_id")
    user_id: str = Field(foreign_key="users.user_id")
    amount: float
    description: str
    date: date


class Media(SQLModel, table=True):
    __tablename__ = "media"

    media_id: Optional[str] = Field(
        default_factory=generate_media_id, primary_key=True, index=True
    )
    trip_id: str = Field(foreign_key="trips.trip_id")
    user_id: str = Field(foreign_key="users.user_id")
    media_url: str
    media_type: MediaType
    uploaded_at: datetime = Field(default_factory=datetime.now)