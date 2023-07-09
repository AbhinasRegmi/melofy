from typing import Optional
from datetime import datetime

from pydantic import Field
from pydantic import BaseModel, ConfigDict

from melofy.schemas.user_schema import UserResponseInsideMusic


class MusicUploadSchema(BaseModel):
    title: str
    cover_url: str

class MusicResponseSchema(MusicUploadSchema):
    id: Optional[int]

    created_at: datetime = Field(default=datetime.now())
    published_by: UserResponseInsideMusic

    model_config = ConfigDict(from_attributes=True)

    