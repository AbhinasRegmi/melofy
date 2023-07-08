from fastapi import APIRouter

from melofy.api.handlers.google_handler import google_handler
from melofy.api.handlers.token_handler import token_handler


auth_router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"]
)

auth_router.include_router(google_handler)
auth_router.include_router(token_handler)