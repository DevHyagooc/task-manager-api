from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Task Manager API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API para gerenciamento de tarefas com FastAPI"

    DATABASE_URL: str = ""

    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()