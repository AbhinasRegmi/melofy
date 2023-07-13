from typing import Generator
from contextlib import contextmanager
from tempfile import NamedTemporaryFile

from fastapi import UploadFile

from melofy.core.config import settings
from melofy.utils.schemas import TemporaryFileType
from melofy.utils.exceptions import UploadMaxSizeExceedError


@contextmanager
def validate_img_size(file: UploadFile) -> Generator[TemporaryFileType, None, None]:
    real_file_size = 0

    with NamedTemporaryFile(delete=False) as tmp:
        for chunk in file.file:
            real_file_size += len(chunk)
            if real_file_size > settings.MELOFY_COVER_UPLOAD_MAXSIZE:
                raise UploadMaxSizeExceedError
            tmp.write(chunk)

        tmp.close()

        yield TemporaryFileType(name=tmp.name, content_type=file.content_type) #type:ignore we are sure there will be content type

@contextmanager
def validate_audio_size(file: UploadFile) -> Generator[TemporaryFileType, None, None]:
    real_file_size = 0

    with NamedTemporaryFile(delete=False) as tmp:
        for chunk in file.file:
            real_file_size += len(chunk)
            if real_file_size > settings.MELOFY_AUDIO_UPLOAD_MAXSIZE:
                raise UploadMaxSizeExceedError
            tmp.write(chunk)

        tmp.close()

        yield TemporaryFileType(name=tmp.name, content_type=file.content_type) #type:ignore
        
        
