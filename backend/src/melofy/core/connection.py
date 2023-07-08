from sqlalchemy import create_engine

from melofy.core.config import settings

engine = create_engine(
    # url=settings.DATABASE_CONNECTION_URI
    url="sqlite:///melofy.db",
    connect_args={
        "check_same_thread": False
    }
)
