from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from melofy.core.config import settings
from melofy.api.auth_router import auth_router
from melofy.api.user_router import user_router
from melofy.api.upload_router import upload_router

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
app.include_router(user_router)
app.include_router(upload_router)
