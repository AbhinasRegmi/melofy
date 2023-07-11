from fastapi import APIRouter

from melofy.api.handlers.music_handler import music_handler

music_router = APIRouter(
    prefix="/upload",
    tags=['upload']
)

music_router.include_router(music_handler)

