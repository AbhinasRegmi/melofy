from fastapi import APIRouter

from melofy.auth.api.google_handler import google_handler


auth_router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"]
)

auth_router.include_router(google_handler)