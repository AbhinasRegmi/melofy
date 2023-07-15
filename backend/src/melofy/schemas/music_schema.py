from typing import Optional
from datetime import datetime

from pydantic import Field, HttpUrl
from pydantic import BaseModel, ConfigDict

from melofy.schemas.user_schema import UserResponseInsideMusic


class MusicResponseSchema(BaseModel):
    id: Optional[int]

    title: str
    cover_url: str
    file_hash: str
    created_at: datetime
    published_by: UserResponseInsideMusic

    model_config = ConfigDict(from_attributes=True)

class MusicMetaUploadSchema(BaseModel):
    title: str
    cover_url: str
    file_hash: str

    created_at: datetime = Field(default=datetime.now())