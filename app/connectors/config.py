from pydantic import PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings for the application, loaded from environment variables.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Neon.tech database credentials
    NEON_USER: str = "your-neon-username"
    NEON_PASSWORD: str = "your-neon-password"
    NEON_HOST: str = "ep-cool-name-123456.us-east-2.aws.neon.tech"
    NEON_DB: str = "your-db-name"
    NEON_TEST_DB: str = "your-test-db-name"

    ADMIN_EMAILS: str
    CLIENT_ID: str
    SECRET_KEY: str = "your-secret-key"
    ALLOWED_DOMAINS: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        """
        Dynamically generate the PostgreSQL database URI for the main database.
        """
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.NEON_USER,
            password=self.NEON_PASSWORD,
            host=self.NEON_HOST,
            path=self.NEON_DB,
        )

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_TEST_URI(self) -> PostgresDsn:
        """
        Dynamically generate the PostgreSQL database URI for the test database.
        """
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.NEON_USER,
            password=self.NEON_PASSWORD,
            host=self.NEON_HOST,
            path=self.NEON_TEST_DB,
        )


# Singleton instance of Settings
settings = Settings()