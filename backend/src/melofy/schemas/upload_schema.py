from enum import Enum
from typing import Any
from itertools import chain

from fastapi import UploadFile
from starlette.datastructures import UploadFile as UP


class UploadImageType(str, Enum):
    jpeg = "image/jpeg"
    png = "image/png"
    bmp = "image/bmp"

class UploadAudioType(str, Enum):
    mp3 = "audio/mpeg"
    mp4 = "audio/mp4"


# ALL_UPLOAD_TYPES = [a.value for a in chain(UploadImageType, UploadAudioType)]
AVAILABLE_IMAGE_TYPES = [a.value for a in UploadImageType]
AVAILABLE_AUDIO_TYPES = [a.value for a in UploadAudioType]

class UploadFileImage(UploadFile):
    @classmethod
    def validate(cls, v: Any) -> Any:
        res: UP = cls.validate(v)

        if not res.content_type in AVAILABLE_IMAGE_TYPES:
            raise ValueError(f"{res.content_type} is not supported for image.")
        
        return res

class UploadFileAudio(UploadFile):
    @classmethod
    def validate(cls, v: Any) -> Any:
        res: UP = cls.validate(v)

        if not res.content_type in AVAILABLE_AUDIO_TYPES:
            raise ValueError(f"{res.content_type} is not supported in audio.")
        
        return res
    