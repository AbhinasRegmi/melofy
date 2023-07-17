from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from melofy.models.user_model import Tags, Music
from melofy.schemas.music_schema import MusicTags

class TagServices:
    @classmethod
    def check_tag(cls, db: Session, tag: MusicTags) -> Optional[Tags]:
        return db.query(Tags).filter(Tags.title==tag.value).first()
    
    @classmethod
    def check_and_create_tags(cls, db: Session, tags: List[MusicTags]) -> List[Tags]:
        tags_db: List[Tags] = []
        for tag in tags:
            if not (tag_db:=TagServices.check_tag(db, tag)):
                tag_db = TagServices.create_tag(db, tag)

            tags_db.append(tag_db)

        return tags_db
    
    @classmethod
    def create_tag(cls, db: Session, tag: MusicTags) -> Tags:
        try:
            db_tab = Tags(
                title=tag.value
            )

            db.add(db_tab)
            db.commit()
            db.refresh(db_tab)

            return db_tab
        except IntegrityError:
            db.rollback()
            raise ValueError(f"The tag `{tag.value}` already exits.")
        
    @classmethod
    def add_music_tag(cls, db: Session, tag: MusicTags, music: Music) -> Tags:
        if not (tag_db:=TagServices.check_tag(db, tag)):
            tag_db= Tags(
                title=tag.value
            )
            tag_db.music.append(music)

            db.add(tag_db)
            db.commit()
            db.refresh(tag_db)

            return tag_db

        db.commit()

        return tag_db