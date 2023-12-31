from fastapi import APIRouter

from melofy.api.handlers.user_handler import user_handler

user_router = APIRouter(
    prefix="/api/v1/user",
    tags=["user"]
)

user_router.include_router(user_handler)