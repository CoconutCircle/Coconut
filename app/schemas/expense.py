from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
from app.models.users import User
from app.schemas.types import TripStatus, InviteStatus, MediaType
from datetime import date


class ExpenseCreate(BaseModel):
    trip_id: str
    amount: float
    description: str
    date: date


class ExpenseRead(BaseModel):
    expense_id: str
    trip_id: str
    user_id: str
    amount: float
    description: str
    date: date
    created_at: datetime
