
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime as dt, timezone
from app.api.deps import SessionDep
from app.core.config import settings
from app.schemas.trips import TripCreate
from app.models.trips import Trip
from app.api.middlewares.token_authorization import get_current_user
from app.crud.trips import create_trip,get_trip

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


router = APIRouter()


@router.post("/")
def create_Trip(*,session: SessionDep,current_user: str = Depends(get_current_user),trip_create : TripCreate )-> Trip:
    try :
        return create_trip(session=session,trip_create=trip_create,created_by=current_user['user_id'])
    except Exception as e:
         raise HTTPException(status_code=400, detail="Failed to create trip")

@router.get("/{trip_id}")
def get_Trip(*,session: SessionDep,trip_id : str)-> Trip:
    try :
        return get_trip(session=session,trip_id=trip_id)
    except Exception as e:
         raise HTTPException(status_code=400, detail="Failed to get trip")


    
    
    