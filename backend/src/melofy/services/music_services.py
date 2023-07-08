from typing import Optional

from sqlalchemy.orm import Session

from melofy.models.user_model import Music, User
from melofy.schemas.music_schema import MusicUploadSchema


class MusicServices:
    @classmethod
    def add_music(cls, db: Session, music: MusicUploadSchema, publisher: User) -> Optional[Music]:
        db_music = Music(
            title=music.title,
            cover_url=music.cover_url,
            publisher_id=publisher.id,
            published_by=publisher
        )

        publisher.published_musics.append(db_music)
        
        db.add(publisher)
        db.commit()
        db.refresh(publisher)

        return db_music