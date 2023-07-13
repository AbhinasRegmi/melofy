from functools import lru_cache

import cloudinary
from pymongo import MongoClient
from sqlalchemy import create_engine


from melofy.core.config import settings

engine = create_engine(
    url="sqlite:///melofy.db",
    connect_args={
        "check_same_thread": False
    }
)

@lru_cache(maxsize=1)
def _get_mongodb():
    db = MongoClient(settings.MONGODB_CONNECTION_URI).melofy
    return db


mongodb_client = _get_mongodb()

#global settings required for cloudinary
#import this in main.py
GLOBAL_CLOUDINARY_CONFIG = cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)
