from fastapi import APIRouter

from melofy.upload.api.music_handler import music_router

upload_router = APIRouter(
    prefix="/upload",
    tags=['upload']
)

upload_router.include_router(music_router)

