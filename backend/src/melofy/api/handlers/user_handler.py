from typing import List

from fastapi import APIRouter, Depends

from melofy.deps.database import get_db
from melofy.deps.security import get_current_user

from melofy.services.user_services import UserServices
from melofy.schemas.music_schema import MusicResponseSchema


user_handler = APIRouter()


@user_handler.get(
        "/all-uploads",
        response_model=List[MusicResponseSchema])
def get_user_uploads(db=Depends(get_db), user=Depends(get_current_user)):
    data = UserServices.get_all_user_music(
        db,
        user.id
    )

    return data