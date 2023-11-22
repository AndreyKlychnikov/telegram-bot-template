import enum
from pathlib import Path
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from pydantic import PostgresDsn, validator
from pydantic_settings import BaseSettings

load_dotenv()


class TelegramBotMode(enum.Enum):
    WEBHOOK = "webhook"
    POLLING = "polling"


class Settings(BaseSettings):
    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    ON_BOT_START_MESSAGE: str
    ON_BOT_HELP_MESSAGE: str
    TELEGRAM_TOKEN: str
    TELEGRAM_MODE: TelegramBotMode = TelegramBotMode.POLLING
    AMPLITUDE_TOKEN: str

    SENTRY_DSN: str | None = None
    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_SERVER"),
                path=values.get("POSTGRES_DB") or "",
            )
        )

    class Config:
        case_sensitive = True


settings = Settings()
