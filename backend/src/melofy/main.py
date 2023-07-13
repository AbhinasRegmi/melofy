from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from melofy.deps.database import MongoDb

from melofy.core.config import settings
from melofy.core.connection import GLOBAL_CLOUDINARY_CONFIG

from melofy.api.auth_router import auth_router
from melofy.api.user_router import user_router
from melofy.api.music_router import music_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    MongoDb.get_connection()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    redoc_url='',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(music_router)
