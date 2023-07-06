from typing import List
from typing import Optional

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from melofy.db.models.base_model import Base
from melofy.core.connection import engine


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str]

    is_verified: Mapped[bool] = mapped_column(default=True)
    published: Mapped[Optional[List["MusicMetaData"]]] = relationship(    #type:ignore
        back_populates="created_by",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(email={self.email}, avatar={self.avatar})"





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