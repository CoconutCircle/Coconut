
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime as dt, timezone
from app.api.deps import SessionDep
from app.core.config import settings
from app.crud.users import get_user_by_email,get_user_trips_by_id,get_user,get_user_friendships,get_user_invites,get_user_expenses,get_user_media
from app.models.users import User
from app.models.trips import Trip
from app.api.middlewares.token_authorization import get_current_user
from app.schemas.users import UserComplete

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


router = APIRouter()


@router.get("/profile")
async def get_Profile(session: SessionDep, current_user: str = Depends(get_current_user))->User:
    """
    Get user profile.
    
    Args:
        session: Database session
        current_user: Current authenticated user from JWT token
        
    Returns:
        User object with all user details
    """
    user = get_user_by_email(
        session=session, email=current_user['email'])
    return user
    
@router.get("/trips")
async def get_Trips(session: SessionDep, current_user: str = Depends(get_current_user))->list[Trip]:
    """
    Get user trips.
    
    Args:
        session: Database session
        current_user: Current authenticated user from JWT token
        
    Returns:
        List of Trip objects
    """
    try :
        trips = get_user_trips_by_id(session=session,user_id=current_user['user_id'])
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to get trips")
    
    return trips


@router.get("/details")
async def get_Complete_User_Details(
    session: SessionDep, 
    current_user: dict = Depends(get_current_user)
) -> UserComplete:
    """
    Get complete user details including profile, trips, friends, invites, expenses, and media.
    
    Args:
        session: Database session
        current_user: Current authenticated user from JWT token
        
    Returns:
        UserComplete object with all user details
    """
    try:
        user_id = current_user['user_id']
        
        # Get basic user profile
        user = get_user(session=session, user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
            
        # Get all associated data
        trips = get_user_trips_by_id(session=session, user_id=user_id)
        friends = get_user_friendships(session=session, user_id=user_id)
        invites = get_user_invites(session=session, user_id=user_id)
        expenses = get_user_expenses(session=session, user_id=user_id)
        media = get_user_media(session=session, user_id=user_id)
        
        # Construct and return the complete response
        return UserComplete(
            user=user,
            trips=trips,
            friends=friends,
            invites=invites,
            expenses=expenses,
            media=media
        )
    except Exception as e:
        # Log the error for debugging
        print(f"Error fetching user details: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve complete user details: {str(e)}"
        )