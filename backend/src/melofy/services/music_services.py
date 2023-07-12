from typing import Optional

from sqlalchemy.orm import Session

from melofy.models.user_model import Music, User


class MusicServices:
    @classmethod
    def add_music(cls, db: Session, title: str, cover_url: str, publisher: User) -> Optional[Music]:
        db_music = Music(
            title=title,
            cover_url=cover_url,
            publisher_id=publisher.id,
            published_by=publisher
        )

        publisher.published_musics.append(db_music)
        
        db.add(publisher)
        db.commit()
        db.refresh(publisher)

        return db_music