from typing import Optional, List

from sqlalchemy.orm import Session

from melofy.services.tag_services import TagServices
from melofy.models.user_model import Music, User, Tags
from melofy.schemas.music_schema import MusicMetaUploadSchema, MusicTags

class MusicServices:
    @classmethod
    def add_music(cls, db: Session, user: User, meta: MusicMetaUploadSchema) -> None:
        """
        Run this as a background task.
        """

        if not meta.file_hash:
            raise ValueError("Valid File Hash Required. Got Empty")
        
        tags_db = TagServices.check_and_create_tags(db, meta.tags)
        
        db_music = Music(
            title=meta.title,
            cover_url=meta.cover_url,
            file_hash=meta.file_hash,
            tags=tags_db,
            publisher_id=user.id,
            published_by=user
        )

        user.published_musics.append(db_music)
        
        db.add(user)
        db.commit()
        db.refresh(user)

    @classmethod
    def get_music_by_tag(cls, db: Session, tag: MusicTags) -> List[Music]:
        return db.query(Music).filter(
            Music.tags.any(Tags.title == tag.value)
        ).all()
    
    @classmethod
    def get_music_by_title(cls, db: Session, title: str) -> List[Music]:
        ...

    