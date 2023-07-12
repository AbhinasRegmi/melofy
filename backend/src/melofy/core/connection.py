import cloudinary
from sqlalchemy import create_engine


from melofy.core.config import settings

engine = create_engine(
    # url=settings.DATABASE_CONNECTION_URI
    url="sqlite:///melofy.db",
    connect_args={
        "check_same_thread": False
    }
)

#global settings required for cloudinary
#import this in main.py
GLOBAL_CLOUDINARY_CONFIG = cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)
