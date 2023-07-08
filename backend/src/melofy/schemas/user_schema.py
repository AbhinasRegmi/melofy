from typing import Optional

from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    id: Optional[int] = None

    email: EmailStr
    avatar: str
    is_verified: Optional[bool] = True

    class Config:
        orm_mode = True

class UserResponseInsideMusic(BaseModel):
    email: EmailStr
    avatar: str

    class Config:
        orm_mode = True