from src.infra.schemas.database.mongodb import MongodbParams
from src.domain.enums import Environment, DBStack
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    
    ENVIRONMENT: Environment
    STRIPE_API_KEY: str
    DB_STACK: DBStack
    MONGODB: MongodbParams
        
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=[
            f".env.{os.getenv("ENVIRONMENT", "dev")}",
            f"../.env.{os.getenv("ENVIRONMENT", "dev")}",
        ],
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings: Settings = Settings()
