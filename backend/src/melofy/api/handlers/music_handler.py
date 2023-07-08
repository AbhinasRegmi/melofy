from fastapi import APIRouter
from fastapi import Body, Depends

from melofy.deps.database import get_db
from melofy.deps.security import get_current_user
from melofy.services.music_services import MusicServices
from melofy.schemas.music_schema import MusicResponseSchema, MusicUploadSchema

music_handler = APIRouter()

#testing route
@music_handler.post("/music", response_model=MusicResponseSchema)
def upload(db = Depends(get_db), user = Depends(get_current_user), music: MusicUploadSchema = Body(...)):
    
    music_db = MusicServices.add_music(
        db,
        music,
        user
    )

    return music_db
