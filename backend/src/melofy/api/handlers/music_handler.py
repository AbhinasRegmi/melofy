from fastapi import Body, Depends
from fastapi import APIRouter, UploadFile, File, Form

from melofy.deps.database import get_db
from melofy.core.config import settings
from melofy.deps.security import get_current_user
from melofy.services.music_services import MusicServices
from melofy.schemas.upload_schema import UploadTypeValidation
from melofy.schemas.music_schema import MusicResponseSchema

music_handler = APIRouter()

#testing route
@music_handler.post("/music")
def upload(
    db=Depends(get_db),
    user=Depends(get_current_user),
    title: str = Form(...),
    cover: UploadFile = File(...),
    music: UploadFile = File(...)):

    #validate file_types
    UploadTypeValidation.validate_type(cover, image=True)
    UploadTypeValidation.validate_type(music, image=False)

    return {
        "msg": "done."
    }