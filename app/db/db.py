from sqlmodel import create_engine

from app.db.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URIL))

test_engine = create_engine(str(settings.SQLALCHEMY_DATABASE_TEST_URI))
