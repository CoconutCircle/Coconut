from sqlmodel import Session, select, or_
from app.schemas.trips import TripCreate, TripInviteCreate
from app.models.trips import Trip, TripMember, TripInvite
from app.schemas.types import MemberRole, TripStatus, InviteStatus
from datetime import datetime
import uuid
from typing import List, Optional
from app.models.users import UserTrip  

def create_trip(*, session: Session, trip_create: TripCreate,created_by:str) -> Trip:
    """
    Create a new trip and automatically set the creator as an admin member.
    
    Args:
        session: Database session
        trip_create: Trip creation data
        
    Returns:
        The newly created Trip object
    """
    # Get current user info from token (should be passed from the API route)
    # For now, assuming trip_create contains created_by field
    
    # Create the trip
    db_obj = Trip(
        trip_name=trip_create.trip_name,
        created_by=created_by, 
        start_date=trip_create.start_date,
        end_date=trip_create.end_date,
        location=trip_create.location,
        is_public=trip_create.is_public,
        trip_status=TripStatus.INCOMING
    )
    
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    
    # Create a TripMember entry for the creator (as ADMIN)
    trip_member = TripMember(
        trip_id=db_obj.trip_id,
        user_id=db_obj.created_by,
        role=MemberRole.ADMIN
    )
    session.add(trip_member)
    
    # Create a UserTrip entry for the creator
    user_trip = UserTrip(
        user_id=db_obj.created_by,
        trip_id=db_obj.trip_id,
        trip_status=TripStatus.INCOMING
    )
    session.add(user_trip)
    
    session.commit()
    session.refresh(db_obj)
    
    return db_obj


def get_trip(*, session: Session, trip_id: str) -> Optional[Trip]:
    """
    Get a trip by its ID
    
    Args:
        session: Database session
        trip_id: ID of the trip to retrieve
        
    Returns:
        Trip object if found, None otherwise
    """
    return session.get(Trip, trip_id)


def update_trip_status(*, session: Session, trip_id: str, new_status: TripStatus) -> Optional[Trip]:
    """
    Update a trip's status
    
    Args:
        session: Database session
        trip_id: ID of the trip to update
        new_status: New status to set
        
    Returns:
        Updated Trip object if found, None otherwise
    """
    trip = session.get(Trip, trip_id)
    if not trip:
        return None
        
    trip.trip_status = new_status
    session.add(trip)
    session.commit()
    session.refresh(trip)
    return trip


def get_trip_members(*, session: Session, trip_id: str) -> List[TripMember]:
    """
    Get all members of a trip
    
    Args:
        session: Database session
        trip_id: ID of the trip
        
    Returns:
        List of TripMember objects
    """
    return session.exec(
        select(TripMember).where(TripMember.trip_id == trip_id)
    ).all()


def create_trip_invite(*, session: Session, invite_create: TripInviteCreate, sender_id: str) -> TripInvite:
    """
    Create a new trip invitation
    
    Args:
        session: Database session
        invite_create: Invitation data
        sender_id: ID of the user sending the invitation
        
    Returns:
        New TripInvite object
    """
    # Generate a unique invite link
    invite_link = f"invite_{uuid.uuid4()}"
    
    invite = TripInvite(
        trip_id=invite_create.trip_id,
        sender_id=sender_id,
        receiver_id=invite_create.receiver_id,
        invite_link=invite_link,
        status=InviteStatus.PENDING
    )
    
    session.add(invite)
    session.commit()
    session.refresh(invite)
    return invite


def update_invite_status(*, session: Session, invite_id: str, new_status: InviteStatus) -> Optional[TripInvite]:
    """
    Update a trip invitation's status
    
    Args:
        session: Database session
        invite_id: ID of the invitation
        new_status: New status to set
        
    Returns:
        Updated TripInvite object if found, None otherwise
    """
    invite = session.get(TripInvite, invite_id)
    if not invite:
        return None
        
    invite.status = new_status
    
    # If accepted, also create a trip member entry
    if new_status == InviteStatus.ACCEPTED:
        trip_member = TripMember(
            trip_id=invite.trip_id,
            user_id=invite.receiver_id,
            role=MemberRole.MEMBER
        )
        session.add(trip_member)
    
    session.add(invite)
    session.commit()
    session.refresh(invite)
    return invite