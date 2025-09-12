from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    EXTERNAL_FASTAPI_PORT: int
    INTERNAL_FASTAPI_PORT: int
    
    STRIPE_API_KEY: str
    
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str
        
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings: Settings = Settings()
