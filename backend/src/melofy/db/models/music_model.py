from datetime import datetime

from melofy.db.models.base_model import Base
from melofy.core.connection import engine

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

class MusicMetaData(Base):
    __tablename__ = "music_metadata"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    created_by: Mapped["User"] = relationship(  #type:ignore
        back_populates="published"
    )

    def __repr__(self) -> str:
        return f"MusicMetaData(title={self.title}, created_by={self.created_by}, created_at={self.created_at})"




def create_all_music() -> None:
    """
    Creates all the tables in the database
    """
    Base.metadata.create_all(bind=engine)

def remove_all_music() -> None:
    """
    Delete all columns in music table.
    """
    Base.metadata.drop_all(bind=engine)
