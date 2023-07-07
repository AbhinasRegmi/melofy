from typing import Generator

from sqlalchemy.orm import Session

from melofy.core.connection import engine


def get_db() -> Generator[Session, None, None]:
    with Session(bind=engine, autocommit=False, autoflush=False) as session:
        yield session