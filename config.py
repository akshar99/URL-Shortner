from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str ="http://localhost:8000"
    db_url: str = "sqlite:///./shortner.db"

def get_settings() -> Settings:
    settings = Settings()
    print(f"returning settings for: {settings.env_name}")
    return settings