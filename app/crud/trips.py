from app.schemas.trips import TripCreate
from app.models.trips import Trip, TripMember
from app.schemas.types import MemberRole
from sqlmodel import Session


def create_trip(*, session: Session,trip_create: TripCreate) -> Trip:
    db_obj = Trip.model_validate(trip_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)

    trip_mem_obj = TripMember.model_validate(
        trip_id=db_obj.trip_id, user_id=db_obj.created_by,role = MemberRole.ADMIN
    )
    session.add(trip_mem_obj)
    session.commit()
    session.refresh(trip_mem_obj)
    return db_obj


def get_trip(*,  session: Session, trip_id: str) -> Trip:
    return session.get(Trip, trip_id)
