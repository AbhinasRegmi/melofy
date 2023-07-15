from typing import Optional

from sqlalchemy.orm import Session

from melofy.models.user_model import Music, User
from melofy.schemas.music_schema import MusicMetaUploadSchema

class MusicServices:
    @classmethod
    def add_music(cls, db: Session, user: User, meta: MusicMetaUploadSchema) -> None:
        """
        Run this as a background task.
        """
        db_music = Music(
            title=meta.title,
            cover_url=meta.cover_url,
            file_hash=meta.file_hash,
            publisher_id=user.id,
            published_by=user
        )

        user.published_musics.append(db_music)
        
        db.add(user)
        db.commit()
        db.refresh(user)