from urllib.parse import urlencode
from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_SERVER: str 
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str 
    POSTGRES_TEST_DB: str 
    SECRET_KEY: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    FRONTEND_URL: str
    

    def _build_dsn(self, db_name: str, query: dict[str, str] | None = None) -> PostgresDsn:
        
        query_str = urlencode(query or {})
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            # port=self.POSTGRES_PORT,
            path=db_name,
            query=query_str, 
        )
    
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        print(self.POSTGRES_DB)
        return self._build_dsn(self.POSTGRES_DB, {"sslmode": "require"})
    
    # @computed_field
    # @property
    # def SQLALCHEMY_DATABASE_STATIC_URI(self) -> PostgresDsn:
    #     return self.POSTGRES_URI
    
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_TEST_URI(self) -> PostgresDsn:
        return self._build_dsn(self.POSTGRES_TEST_DB, {"sslmode": "require"})

settings = Settings()