from functools import lru_cache

import cloudinary
from sqlalchemy import create_engine
from motor.motor_asyncio import AsyncIOMotorClient


from melofy.core.config import settings

engine = create_engine(
    url="sqlite:///melofy.db",
    connect_args={
        "check_same_thread": False
    }
)

@lru_cache(maxsize=1)
def _get_mongodb():
    db = AsyncIOMotorClient(settings.MONGODB_CONNECTION_URI).melofy
    return db


mongodb = _get_mongodb()

#global settings required for cloudinary
#import this in main.py
GLOBAL_CLOUDINARY_CONFIG = cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)
