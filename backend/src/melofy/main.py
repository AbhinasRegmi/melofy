from fastapi import FastAPI

from melofy.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    redoc_url=''
)
