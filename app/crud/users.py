from sqlmodel import Session, select, or_
from typing import List, Optional, Dict, Any
from datetime import datetime

from app.models.users import User, UserTrip, Friendship
from app.models.trips import Trip, TripMember, TripInvite
from app.models.tripdetails import Expense, Media, Itinerary
from app.schemas.users import UserCreate, UserUpdate
from app.schemas.types import FriendshipStatus, TripStatus


def create_user(*, session: Session, user_create: UserCreate) -> User:
    """
    Create a new user in the database.
    
    Args:
        session: Database session
        user_create: User creation data
        
    Returns:
        The newly created User object
    """
    db_obj = User.model_validate(user_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(*, session: Session, email: str) -> Optional[User]:
    """
    Get a user by email address.
    
    Args:
        session: Database session
        email: Email address to look for
        
    Returns:
        User object if found, None otherwise
    """
    return session.exec(select(User).where(User.email == email)).first()


def get_user(*, session: Session, user_id: str) -> Optional[User]:
    """
    Get a user by ID.
    
    Args:
        session: Database session
        user_id: User ID to look for
        
    Returns:
        User object if found, None otherwise
    """
    return session.get(User, user_id)


def get_users(*, session: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """
    Get multiple users with pagination.
    
    Args:
        session: Database session
        skip: Number of users to skip
        limit: Maximum number of users to return
        
    Returns:
        List of User objects
    """
    return session.exec(select(User).offset(skip).limit(limit)).all()


def update_user(*, session: Session, db_obj: User, obj_in: UserUpdate) -> User:
    """
    Update a user.
    
    Args:
        session: Database session
        db_obj: Existing user object
        obj_in: Update data
        
    Returns:
        Updated User object
    """
    update_data = obj_in.model_dump(exclude_unset=True)
    
    for field in update_data:
        setattr(db_obj, field, update_data[field])
        
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def delete_user(*, session: Session, user_id: str) -> bool:
    """
    Delete a user.
    
    Args:
        session: Database session
        user_id: ID of the user to delete
        
    Returns:
        True if deleted, False if not found
    """
    user = session.get(User, user_id)
    if not user:
        return False
        
    session.delete(user)
    session.commit()
    return True


def get_user_trips_by_id(*, session: Session, user_id: str, status: Optional[TripStatus] = None) -> List[Trip]:
    """
    Get all trips associated with a user by their user_id.
    
    This includes:
    1. Trips where the user is directly linked via UserTrip
    2. Trips created by the user
    3. Trips where the user is a member
    
    Args:
        session: The database session
        user_id: The ID of the user
        status: Optional trip status filter
        
    Returns:
        A list of Trip objects associated with the user
    """
    # First, get all trips from UserTrip association
    user_trip_ids = session.exec(
        select(UserTrip.trip_id).where(UserTrip.user_id == user_id)
    ).all()
    
    # Then get trips where user is a member
    member_trip_ids = session.exec(
        select(TripMember.trip_id).where(TripMember.user_id == user_id)
    ).all()
    
    # Build base query
    query = select(Trip).where(
        or_(
            Trip.created_by == user_id,
            Trip.trip_id.in_(user_trip_ids),
            Trip.trip_id.in_(member_trip_ids)
        )
    )
    
    # Add status filter if provided
    if status:
        query = query.where(Trip.trip_status == status)
    
    # Execute the query and return results
    trips = session.exec(query).all()
    return trips


def create_user_trip(*, session: Session, user_id: str, trip_id: str, trip_status: TripStatus = TripStatus.INCOMING) -> UserTrip:
    """
    Create an association between a user and a trip.
    
    Args:
        session: Database session
        user_id: ID of the user
        trip_id: ID of the trip
        trip_status: Status of the trip for this user
        
    Returns:
        New UserTrip object
    """
    user_trip = UserTrip(
        user_id=user_id,
        trip_id=trip_id,
        trip_status=trip_status
    )
    
    session.add(user_trip)
    session.commit()
    session.refresh(user_trip)
    return user_trip


def create_friendship(*, session: Session, user_id_1: str, user_id_2: str) -> Friendship:
    """
    Create a new friendship request.
    
    Args:
        session: Database session
        user_id_1: ID of the user sending the request
        user_id_2: ID of the user receiving the request
        
    Returns:
        New Friendship object
    """
    # Check if friendship already exists in either direction
    existing = session.exec(
        select(Friendship).where(
            or_(
                (Friendship.user_id_1 == user_id_1) & (Friendship.user_id_2 == user_id_2),
                (Friendship.user_id_1 == user_id_2) & (Friendship.user_id_2 == user_id_1)
            )
        )
    ).first()
    
    if existing:
        return existing
    
    friendship = Friendship(
        user_id_1=user_id_1,
        user_id_2=user_id_2,
        status=FriendshipStatus.PENDING
    )
    
    session.add(friendship)
    session.commit()
    session.refresh(friendship)
    return friendship


def update_friendship_status(*, session: Session, friendship_id: str, new_status: FriendshipStatus) -> Optional[Friendship]:
    """
    Update a friendship status.
    
    Args:
        session: Database session
        friendship_id: ID of the friendship
        new_status: New status to set
        
    Returns:
        Updated Friendship object if found, None otherwise
    """
    friendship = session.get(Friendship, friendship_id)
    if not friendship:
        return None
        
    friendship.status = new_status
    session.add(friendship)
    session.commit()
    session.refresh(friendship)
    return friendship


def get_user_friendships(*, session: Session, user_id: str, status: Optional[FriendshipStatus] = None) -> List[Friendship]:
    """
    Get all friendships for a user.
    
    Args:
        session: Database session
        user_id: ID of the user
        status: Optional status filter
        
    Returns:
        List of Friendship objects
    """
    query = select(Friendship).where(
        or_(
            Friendship.user_id_1 == user_id,
            Friendship.user_id_2 == user_id
        )
    )
    
    if status:
        query = query.where(Friendship.status == status)
        
    return session.exec(query).all()


def get_user_expenses(*, session: Session, user_id: str) -> List[Expense]:
    """
    Get all expenses created by a user.
    
    Args:
        session: Database session
        user_id: ID of the user
        
    Returns:
        List of Expense objects
    """
    return session.exec(
        select(Expense).where(Expense.user_id == user_id)
    ).all()


def get_user_media(*, session: Session, user_id: str) -> List[Media]:
    """
    Get all media uploaded by a user.
    
    Args:
        session: Database session
        user_id: ID of the user
        
    Returns:
        List of Media objects
    """
    return session.exec(
        select(Media).where(Media.user_id == user_id)
    ).all()


def get_user_invites(*, session: Session, user_id: str, status: Optional[FriendshipStatus] = None) -> List[TripInvite]:
    """
    Get all trip invitations for a user.
    
    Args:
        session: Database session
        user_id: ID of the user
        status: Optional status filter
        
    Returns:
        List of TripInvite objects
    """
    query = select(TripInvite).where(TripInvite.receiver_id == user_id)
    
    if status:
        query = query.where(TripInvite.status == status)
        
    return session.exec(query).all()


def search_users(*, session: Session, query: str, limit: int = 10) -> List[User]:
    """
    Search for users by name or email.
    
    Args:
        session: Database session
        query: Search string
        limit: Maximum number of results
        
    Returns:
        List of matching User objects
    """
    search_pattern = f"%{query}%"
    return session.exec(
        select(User).where(
            or_(
                User.name.like(search_pattern),
                User.email.like(search_pattern)
            )
        ).limit(limit)
    ).all()