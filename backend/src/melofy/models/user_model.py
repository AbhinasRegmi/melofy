from typing import List
from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from melofy.models.base_model import Base
from melofy.core.connection import engine


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str]

    is_verified: Mapped[bool] = mapped_column(default=True)
    # published: Mapped[Optional[List["MusicMetaData"]]] = relationship(
    #     back_populates="created_by",
    #     cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"User(email={self.email}, avatar={self.avatar})"


class MusicMetaData(Base):
    __tablename__ = "music_metadata"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    cover_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    # created_by: Mapped["User"] = relationship(
    #     back_populates="published"
    # )

    def __repr__(self) -> str:
        return f"MusicMetaData(title={self.title}, created_at={self.created_at})"





def create_all_user() -> None:
    """
    Creates all the database models.
    """
    Base.metadata.create_all(bind=engine)


def remove_all_user() -> None:
    """
    Delete all tables in user.
    """
    Base.metadata.drop_all(bind=engine)