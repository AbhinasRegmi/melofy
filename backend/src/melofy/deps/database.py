from typing import Generator

from sqlalchemy.orm import Session

from melofy.core.connection import get_session


def get_db() -> Generator[Session, None, None]:
    return get_session()