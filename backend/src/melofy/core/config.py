"""
All project settings are configured here.
"""

from typing import List
from functools import lru_cache

from pydantic import BaseSettings


class _Setting(BaseSettings):
    class Config:
        env_file: str = ".env"
        case_sensitive: bool = True

    PROJECT_NAME: str = "melofy"
    PROJECT_VERSION: str = "1.0.0"

    CORS_ALLOWED_ORIGINS: List[str] = [
        "https://abhinasregmi.com.np",
        "http://localhost:5500",
    ]


@lru_cache
def _setting() -> _Setting:
    return _Setting() #type:ignore


settings = _setting()
