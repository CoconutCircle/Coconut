from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from app.connectors.db import engine


def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get a database session.

    Yields:
        Session: A SQLModel database session.
    """
    with Session(engine) as session:
        yield session


# Dependency type for FastAPI endpoints
SessionDep = Annotated[Session, Depends(get_db)]