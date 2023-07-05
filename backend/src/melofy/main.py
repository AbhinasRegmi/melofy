from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from melofy.core.config import settings
from melofy.auth.auth_router import auth_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    redoc_url='',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth_router)
