from fastapi import Header

from melofy.core.config import settings


async def validate_content_length(
        content_length: int = Header(
            ...,
            lt=settings.MELOFY_AUDIO_UPLOAD_MAXSIZE)):
    return content_length