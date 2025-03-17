from sqlmodel import create_engine

from app.core.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

test_engine = create_engine(str(settings.SQLALCHEMY_DATABASE_TEST_URI))
