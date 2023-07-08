from fastapi import APIRouter, Depends

from melofy.deps.security import get_current_user

music_router = APIRouter()

#testing route
@music_router.get("/music")
def upload(user = Depends(get_current_user)):
    return user