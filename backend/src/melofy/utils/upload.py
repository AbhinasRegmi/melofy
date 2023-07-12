from typing import IO
from tempfile import NamedTemporaryFile

from fastapi import UploadFile

from melofy.core.config import settings


# def validate_upload_size(file: UploadFile, file_type:):
#     real_file_size: int = 0