from fastapi import Depends, BackgroundTasks
from fastapi import APIRouter, UploadFile, File, Form

from melofy.deps.database import get_db, get_mdb
from melofy.deps.security import get_current_user

from melofy.schemas.upload_schema import UploadTypeValidation

from melofy.services.mongo_services import MongoServices
from melofy.services.cloudinary_services import CloudinaryServices

from melofy.utils.hash import generate_random_hash
from melofy.utils.upload import validate_img_size, validate_audio_size


music_handler = APIRouter()

#testing route
@music_handler.post("/music")
async def upload(
    background: BackgroundTasks,
    db=Depends(get_db),
    mdb=Depends(get_mdb),
    user=Depends(get_current_user),
    title: str = Form(...),
    cover: UploadFile = File(...),
    music: UploadFile = File(...)):

    #validate file_types
    UploadTypeValidation.validate_type(cover, image=True)
    UploadTypeValidation.validate_type(music, image=False)

    #validate file_size
    with validate_img_size(cover) as cover_file:
        # url, tag = CloudinaryServices.upload_image(cover_file)
        pass

    with validate_audio_size(music) as music_file:
        music_hash = generate_random_hash()
        oid = MongoServices.upload_music(mdb, music_file, music_hash)

    return {
        "url": oid,
        "tag": ''
    }