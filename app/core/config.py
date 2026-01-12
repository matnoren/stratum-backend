from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Stratum"
    DATABASE_URL: str = "sqlite:///./stratum.db"

    class Config:
        env_file = ".env"


settings = Settings()
