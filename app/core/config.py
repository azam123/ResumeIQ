from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ResumeIQ"
    env: str = "development"
    anthropic_api_key: str
    anthropic_model: str = "claude-3-7-sonnet-20250219"
    anthropic_base_url: str = "https://api.anthropic.com"
    api_v1_prefix: str = "/api/v1"
    request_timeout_seconds: float = 45.0

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
