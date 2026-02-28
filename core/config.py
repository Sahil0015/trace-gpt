"""Settings via pydantic-settings (placeholder)."""

from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "trace-gpt"

settings = Settings()
