from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from melofy.schemas.user_schema import UserResponseInsideMusic


class MusicUploadSchema(BaseModel):
    title: str
    cover_url: str

class MusicResponseSchema(MusicUploadSchema):
    id: Optional[int]

    created_at: datetime = Field(default=datetime.now())
    published_by: UserResponseInsideMusic

    class Config:
        orm_mode = True