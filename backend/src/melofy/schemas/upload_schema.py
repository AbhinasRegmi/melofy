from enum import Enum

from fastapi import UploadFile

from melofy.schemas.exceptions import InvalidImageFormat, InvalidAudioFormat

class ImageType(str, Enum):
    jpeg = "image/jpeg"
    png = "image/png"
    bmp = "image/bmp"

class AudioType(str, Enum):
    mp3 = "audio/mpeg"
    mp4 = "audio/mp4"


# ALL_UPLOAD_TYPES = [a.value for a in chain(ImageType, AudioType)]
AVAILABLE_IMAGE_TYPES = [a.value for a in ImageType]
AVAILABLE_AUDIO_TYPES = [a.value for a in AudioType]

class UploadTypeValidation:
    @classmethod
    def validate_type(cls, file: UploadFile, image: bool = True) -> None:
        if image:
            if file.content_type not in AVAILABLE_IMAGE_TYPES:
                raise InvalidImageFormat(file.content_type)
        else:
            if file.content_type not in AVAILABLE_AUDIO_TYPES:
                raise InvalidAudioFormat(file.content_type)