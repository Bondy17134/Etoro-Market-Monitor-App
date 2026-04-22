from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import uuid

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        case_sensitive=False,
        extra="ignore"
    )
    request_id: str = str(uuid.uuid4())
    api_key: str 
    user_key: str 
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

@lru_cache
def get_setting() -> Settings:
    settings = Settings()
    print(f"Loading setting for : {settings.request_id}")
    return settings