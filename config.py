from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "WorkHour"
    admin_email: str
    database_url: str
    secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()