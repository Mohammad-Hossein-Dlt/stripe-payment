from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    STRIPE_API_KEY: str
        
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str
        
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings: Settings = Settings()
