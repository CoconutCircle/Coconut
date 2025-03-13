"""
    Configuration file
"""
from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
        Settings from env variables 
    """
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "placement"
    POSTGRES_TEST_DB: str = "placement_test"
    SECRET_KEY: str
    POSTGRES_URI: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        """
            This is to dynamically generate database uri
        """
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=f"/{self.POSTGRES_DB}",
        )
    
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URIL(self) -> PostgresDsn:
        return self.POSTGRES_URI
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_TEST_URI(self) -> PostgresDsn:
        """
            This is to dynamically generate test database uri
        """
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=f"/{self.POSTGRES_TEST_DB}",
        )

settings = Settings()
