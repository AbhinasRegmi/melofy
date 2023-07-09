"""
All project settings are configured here.
"""

from typing import List
from functools import lru_cache

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class _Setting(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

    PROJECT_NAME: str = "melofy"
    PROJECT_VERSION: str = "1.0.0"

    CORS_ALLOWED_ORIGINS: List[str] = [
        "https://abhinasregmi.com.np",
        "http://localhost:5500",
        "http://localhost:8000"
    ]

    #jwt
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXP: int = 15 # 15 minutes
    JWT_REFRESH_TOKEN_EXP: int = 7 * 24 * 60 # 7 days

    #smtp
    GOOGLE_SMTP_PORT: int = 465
    GOOGLE_SMTP_HOST: str = "smtp.gmail.com"

    # google endpoints
    GOOGLE_OAUTH_ROOT_URL: str = "https://accounts.google.com/o/oauth2/v2/auth"
    GOOGLE_OAUTH_TOKEN_URL: str = "https://oauth2.googleapis.com/token"
    GOOGLE_OAUTH_USER_URL: str = "https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token="

    # google scopes
    GOOGLE_USER_PROFILE_SCOPE_URL: str = "https://www.googleapis.com/auth/userinfo.profile"
    GOOGLE_USER_EMAIL_SCOPE_URL: str = "https://www.googleapis.com/auth/userinfo.email"

    #callbacks
    GOOGLE_CALLBACK_URL: str = "http://localhost:8000/api/v1/auth/google/callback"

    #.env
    GOOGLE_OAUTH_CLIENT_SECRET: str
    GOOGLE_OAUTH_CLIENT_ID: str

    MELOFY_SMTP_LOGIN: EmailStr
    GOOGLE_SMTP_LOGIN: EmailStr
    GOOGLE_SMTP_PASS: str

    DATABASE_CONNECTION_URI: str

    JWT_ACCESS_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str

@lru_cache
def _setting() -> _Setting:
    return _Setting() #type:ignore


settings = _setting()
