from typing import List

from fastapi import Depends
from fastapi import APIRouter

from melofy.deps.database import get_db
from melofy.deps.security import get_current_user
from melofy.services.user_services import UserServices
from melofy.schemas.music_schema import MusicResponseSchema

user_handler = APIRouter(
    prefix="/user"
)


@user_handler.get("/all-uploads", response_model=List[MusicResponseSchema] | None)
def get_personal_uploads(db = Depends(get_db), user = Depends(get_current_user)):
    return UserServices.get_all_user_music(
        db,
        user.id
    )