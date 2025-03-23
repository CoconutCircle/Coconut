from collections.abc import Generator
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel
from app.core.db import engine


def get_db() -> Generator[Session, None, None]:
    # create_db_and_tables()
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)