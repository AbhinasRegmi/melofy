from typing import Optional

from pydantic import EmailStr
from sqlalchemy.orm import Session

from melofy.db.models.user_model import User
from melofy.db.schemas.user_schema import UserCreateSchema

class UserServices:
    @classmethod
    def create_user(cls, db: Session, user_in: UserCreateSchema) -> Optional[User]:
        db_user = User(
            email=user_in.email,
            avatar=user_in.avatar,
            is_verified=user_in.is_verified
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
    
    @classmethod
    def get_user_by_email(cls, db: Session, email_in: EmailStr) -> Optional[User]:
        return db.query(User).filter(User.email == email_in).first()