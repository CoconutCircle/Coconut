from sqlmodel import create_engine, SQLModel
from app.connectors.config import settings

# Create the main database engine
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

# Create the test database engine
test_engine = create_engine(str(settings.SQLALCHEMY_DATABASE_TEST_URI))


def create_db_and_tables():
    """
    Create all database tables defined in SQLModel models.
    """
    SQLModel.metadata.create_all(engine)


def create_test_db_and_tables():
    """
    Create all database tables in the test database.
    """
    SQLModel.metadata.create_all(test_engine)