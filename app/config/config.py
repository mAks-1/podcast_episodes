from pathlib import Path

from pydantic import BaseModel, PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 20


class Settings(BaseSettings):
    DB_URL: PostgresDsn
    DB_ECHO: bool = False
    DB_ECHO_POOL: bool = False
    DB_POOL_SIZE: int = 50
    DB_MAX_OVERFLOW: int = 20

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        case_sensitive=False,
        extra="ignore",
    )

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

    @property
    def db(self) -> DBConfig:
        return DBConfig(
            url=self.DB_URL,
            echo=self.DB_ECHO,
            echo_pool=self.DB_ECHO_POOL,
            pool_size=self.DB_POOL_SIZE,
            max_overflow=self.DB_MAX_OVERFLOW
        )



settings = Settings()
