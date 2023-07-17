from enum import Enum
from datetime import datetime
from typing import Optional, List

from pydantic import Field, HttpUrl
from pydantic import BaseModel, ConfigDict

from melofy.schemas.user_schema import UserResponseInsideMusic


class MusicTags(str, Enum):
    pop = "pop"
    hip_hop = "hip_hop"
    rock = "rock"
    latin = "latin"
    mood = "mood"
    indie = "indie"
    workout = "workout"
    country = "country"
    chill = "chill"
    sleep = "sleep"
    party = "party"
    at_home = "at_home"
    love = "love"
    metal = "metal"
    jazz = "jazz"
    anime = "anime"
    nepali = "nepali"
    focus = "focus"
    classical = "classical"
    soul = "soul"
    blues = "blues"
    punk = "punk"
    travel = "travel"
    summer = "summer"

class MusicResponseSchema(BaseModel):
    id: Optional[int]

    title: str
    cover_url: str
    file_hash: str
    created_at: datetime
    published_by: UserResponseInsideMusic

    model_config = ConfigDict(from_attributes=True)


class MusicMetaMinimalUploadSchema(BaseModel):
    title: str
    tags: List[MusicTags]


class MusicMetaUploadSchema(MusicMetaMinimalUploadSchema):
    cover_url: str
    file_hash: str

    created_at: datetime = Field(default=datetime.now())