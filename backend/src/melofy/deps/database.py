from typing import Any, Generator
from functools import lru_cache

from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorGridFSBucket

from melofy.core.config import settings
from melofy.core.connection import engine


def get_db() -> Generator[Session, None, None]:
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        yield session

class MongoDb:
    _mclient = None

    @classmethod
    def get_connection(cls) -> None:
        if not cls._mclient:
            db = AsyncIOMotorClient(settings.MONGODB_CONNECTION_URI).melofy
            cls._mclient = AsyncIOMotorGridFSBucket(db)

    @lru_cache(maxsize=1)
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return MongoDb._mclient