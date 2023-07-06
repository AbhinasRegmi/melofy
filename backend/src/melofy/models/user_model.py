from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from melofy.models.base_model import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str]

    is_verified: Mapped[bool] = mapped_column(default=True)

    def __repr__(self) -> str:
        return f"User(email={self.email}, avatar={self.avatar})"
