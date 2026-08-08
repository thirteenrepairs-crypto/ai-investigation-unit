from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AIIU API"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://aiiu:aiiu@localhost:5432/aiiu"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
