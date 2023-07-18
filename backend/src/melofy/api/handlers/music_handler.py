from typing import List

from fastapi.responses import StreamingResponse
from fastapi import Depends, BackgroundTasks, Query
from fastapi import APIRouter, UploadFile, File, Form

from melofy.deps.security import login_required
from melofy.deps.database import get_db, get_mdb
from melofy.deps.security import get_current_user

from melofy.schemas.upload_schema import UploadTypeValidation
from melofy.schemas.music_schema import MusicMetaUploadSchema, MusicTags, MusicResponseSchema

from melofy.services.mongo_services import MongoServices
from melofy.services.music_services import MusicServices
from melofy.services.cloudinary_services import CloudinaryServices

from melofy.utils.hash import generate_random_hash
from melofy.utils.youtube import GetMusicFromYoutube
from melofy.utils.exceptions import Mp4AudioNotFoundError
from melofy.utils.upload import validate_img_size, validate_audio_size


music_handler = APIRouter()


@music_handler.post("/upload")
def upload(
    background: BackgroundTasks,
    db=Depends(get_db),
    mdb=Depends(get_mdb),
    user=Depends(get_current_user),
    title: str = Form(...),
    tags: List[MusicTags] = Form(...),
    cover: UploadFile = File(...),
    music: UploadFile = File(...)):

    #validate file_types
    UploadTypeValidation.validate_type(cover, image=True)
    UploadTypeValidation.validate_type(music, image=False)

    #validate file_size
    file_hash = generate_random_hash()
    with validate_img_size(cover) as cover_file:
        url = CloudinaryServices.upload_image(cover_file, file_hash)

    with validate_audio_size(music) as music_file:
        background.add_task(MongoServices.upload_music, mdb, music_file, file_hash)

    upload_meta = MusicMetaUploadSchema(title=title, tags=tags, cover_url=url, file_hash=file_hash)
    background.add_task(MusicServices.add_music, db, user, upload_meta)
    
    return {
        "msg": "OK"
    }

@music_handler.post("/youtubeupload")
def upload_music_from_youtube(
    background: BackgroundTasks,
    db = Depends(get_db),
    mdb = Depends(get_mdb),
    user = Depends(get_current_user),
    title: str = Form(...),
    music_url: str = Form(...),
    tags: List[MusicTags] = Form(...),
    cover: UploadFile = File(...)):

    #cannot validate audio size

    #validate file types
    file_hash = generate_random_hash()

    with validate_img_size(cover) as cover_file:
        url = CloudinaryServices.upload_image(cover_file, file_hash)

    try:
        with GetMusicFromYoutube(music_url) as music_file:
            background.add_task(MongoServices.upload_music, mdb, music_file, file_hash)
    except ValueError:
        raise Mp4AudioNotFoundError
    
    upload_meta = MusicMetaUploadSchema(title=title, tags=tags, cover_url=url, file_hash=file_hash)
    background.add_task(MusicServices.add_music, db, user, upload_meta)
    
    return {
        "msg": "OK"
    }
        


@music_handler.get(
    "/stream",
    # dependencies=[Depends(login_required)],
    response_class=StreamingResponse)
def stream_music(
    mdb=Depends(get_mdb),
    hash: str=Query(...)
    ):

    content_type, streamer = MongoServices.stream_music(mdb, file_hash=hash)

    return StreamingResponse(
        streamer,
        media_type=content_type
    )

@music_handler.get(
        "/tag",
        response_model=List[MusicResponseSchema],
        dependencies=[Depends(login_required)])
def get_music_by_tag(
    db = Depends(get_db),
    tag: MusicTags = Query(...)):
    return MusicServices.get_music_by_tag(db, tag)