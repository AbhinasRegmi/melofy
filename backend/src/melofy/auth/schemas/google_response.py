from pydantic import BaseModel, Field


class GoogleTokenResponse(BaseModel):
    access_token: str = Field(...)
    id_token: str = Field(...)