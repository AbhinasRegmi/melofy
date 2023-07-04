"""
All project settings are configured here.
"""

from functools import lru_cache

from pydantic import BaseSettings


class _Setting(BaseSettings):
    class Config:
        env_file: str = ".env"
        case_sensitive: bool = True

    PROJECT_NAME: str = "melofy"
    PROJECT_VERSION: str = "1.0.0"


@lru_cache
def _setting() -> _Setting:
    return _Setting() #type:ignore


settings = _setting()
