from pydantic import Field
from pydantic import BaseModel, EmailStr


class GoogleTokenResponse(BaseModel):
    access_token: str = Field(...)
    id_token: str = Field(...)

class GoogleUserDetailResponse(BaseModel):
    email: EmailStr = Field(...)
    avatar: str = Field(...)
    verified: bool = Field(...)