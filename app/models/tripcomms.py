from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from app.models.modelutils import TimestampMixin
from typing import Optional, TYPE_CHECKING
from app.models.base import generate_chat_id

if TYPE_CHECKING:
    from app.models.trips import Trip
    from app.models.users import User


class Chat(SQLModel, table=True):
    __tablename__ = "chats"
    
    message_id: Optional[str] = Field(
        default_factory=generate_chat_id, primary_key=True, index=True
    )
    trip_id: str = Field(foreign_key="trips.trip_id")
    user_id: str = Field(foreign_key="users.user_id")
    message: str
    timestamp: datetime = Field(default_factory=datetime.now)