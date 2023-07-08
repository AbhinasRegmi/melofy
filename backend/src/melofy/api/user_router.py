from fastapi import APIRouter

from melofy.api.handlers.user_handler import user_handler

user_router = APIRouter(
    tags=["users"]
)

user_handler.include_router(user_handler)