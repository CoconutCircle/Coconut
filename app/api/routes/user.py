
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime as dt, timezone
from app.api.deps import SessionDep
from app.core.config import settings
from app.crud.users import get_user_by_email,get_user_trips_by_id
from app.models.users import User
from app.models.trips import Trip
from app.api.middlewares.token_authorization import get_current_user

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


router = APIRouter()


@router.get("/profile")
async def get_Profile(session: SessionDep, current_user: str = Depends(get_current_user))->User:
    user = get_user_by_email(
        session=session, email=current_user['email'])
    return user
    
@router.get("/trips")
async def get_Trips(session: SessionDep, current_user: str = Depends(get_current_user))->list[Trip]:
    try :
        trips = get_user_trips_by_id(session=session,user_id=current_user['user_id'])
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to get trips")
    
    return trips


