from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic import EmailStr

class UserCreateSchema(BaseModel):
    id: Optional[int] = None

    email: EmailStr
    avatar: str
    is_verified: Optional[bool] = True

    model_config = ConfigDict(from_attributes=True)

class UserResponseInsideMusic(BaseModel):
    email: EmailStr
    avatar: str

    model_config = ConfigDict(from_attributes=True)