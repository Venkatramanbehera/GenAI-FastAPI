import os
from  pydantic_settings import BaseSettings

class Settings(BaseSettings):

    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    
    APP_NAME: str = "GenAI Learning Hub"
    DEBUG_MODE: bool = True

    class Config: 
        env_file = ".env"

settings = Settings()