from sqlmodel import Session, select

from app.models import User
from app.schemas.users import UserCreate


def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(user_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def get_user_by_email(*, session: Session, email: str) -> User:
    return session.exec(select(User).where(User.email == email)).first()


def get_user(*, session: Session, user_id: int) -> User:
    return session.get(User, user_id)

def get_users(*, session: Session) -> list[User]:
    return session.exec(select(User)).all()