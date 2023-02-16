from pydantic import BaseSettings, AnyHttpUrl
from typing import List
from decouple import config


class Settings(BaseSettings):
    API: str = "/api"
    MAIL: str = config("MAIL", cast=str)
    MAIL_PASS: str = config("MAIL_PASS", cast=str)
    MAIL_SERVER: str = config("MAIL_SERVER", cast=str)
    MAIL_PORT: str = config("MAIL_PORT", cast=int)
    RECIEVER_MAIL: str = config("RECIEVER_MAIL", cast=str)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "https://theyummyservings.co.uk",
        "http://127.0.0.1:5500/",
    ]
    PROJECT_NAME: str = "TheYummyServings"

    class Config:
        case_sensitive = True


settings = Settings()
