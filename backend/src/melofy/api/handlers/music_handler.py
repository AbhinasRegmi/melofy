from fastapi import Body, Depends
from fastapi import APIRouter, UploadFile, File

from melofy.deps.database import get_db
from melofy.core.config import settings
from melofy.deps.security import get_current_user
from melofy.deps.header import validate_content_length
from melofy.services.music_services import MusicServices
from melofy.schemas.music_schema import MusicResponseSchema, MusicUploadSchema

music_handler = APIRouter()

#testing route
@music_handler.post(
        "/music",
        response_model=MusicResponseSchema,
        dependencies=[Depends(validate_content_length)])
def upload(
    db=Depends(get_db),
    user=Depends(get_current_user),
    metadata_music: MusicUploadSchema=Body(...),
    cover: UploadFile = File(...),
    music: UploadFile = File(...)):
    
    music_db = MusicServices.add_music(
        db,
        metadata_music,
        user
    )

    return music_db
