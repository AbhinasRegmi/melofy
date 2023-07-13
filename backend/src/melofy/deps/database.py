from typing import Any, Generator
from functools import lru_cache


import gridfs
from sqlalchemy.orm import Session

from melofy.core.config import settings
from melofy.core.connection import engine
from melofy.core.connection import mongodb_client


def get_db() -> Generator[Session, None, None]:
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        yield session

def get_mdb() -> gridfs.GridFS:
    fs = gridfs.GridFS(mongodb_client)
    return fs