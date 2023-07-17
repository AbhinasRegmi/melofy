from typing import List
from datetime import datetime

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship, mapped_column


from melofy.models.base_model import Base
from melofy.core.connection import engine



music_tags_association = Table(
    "music_tags_association",
    Base.metadata,
    Column("music_data_id", ForeignKey("music_data.id"), primary_key=True),
    Column("tags_id", ForeignKey("tags.id"), primary_key=True)
)


class Tags(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)

    music: Mapped[List['Music']] = relationship(
        secondary=music_tags_association,
        back_populates='tags'
    )


    def __repr__(self) -> str:
        return f"Tags(title={self.title})"




class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str]

    is_verified: Mapped[bool] = mapped_column(default=True)
    published_musics: Mapped[List["Music"]] = relationship(
        back_populates="published_by"
    )

    def __repr__(self) -> str:
        return f"User(email={self.email}, avatar={self.avatar})"


class Music(Base):
    __tablename__ = "music_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    cover_url: Mapped[str]
    file_hash: Mapped[str]
    tags: Mapped[List[Tags]] = relationship(
        secondary=music_tags_association,
        back_populates="music"
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    publisher_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    published_by: Mapped["User"] = relationship(
        back_populates="published_musics"
    )

    def __repr__(self) -> str:
        return f"Music(title={self.title}, created_at={self.created_at})"



def create_all() -> None:
    """
    Creates all the database models.
    """
    Base.metadata.create_all(bind=engine)


def remove_all() -> None:
    """
    Delete all tables in user.
    """
    Base.metadata.drop_all(bind=engine)