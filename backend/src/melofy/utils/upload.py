from tempfile import NamedTemporaryFile

from fastapi import UploadFile

from melofy.core.config import settings
from melofy.utils.schemas import TemporaryFileType
from melofy.utils.exceptions import UploadMaxSizeExceedError



def validate_img_size(file: UploadFile):
    """
    Don't forget to close the tempfile after use.
    """
    real_file_size = 0
    temp = NamedTemporaryFile(delete=False)
    

    for chunk in file.file:
        real_file_size += len(chunk)
        if real_file_size > settings.MELOFY_COVER_UPLOAD_MAXSIZE:
            raise UploadMaxSizeExceedError
        temp.write(chunk)
    
    temp.close()
    return TemporaryFileType(name=temp.name, file=temp.file)


def validate_audio_size(file: UploadFile) -> TemporaryFileType:
    real_file_size = 0
    temp = NamedTemporaryFile(delete=False)

    for chunk in file.file:
        real_file_size += len(chunk)
        if real_file_size > settings.MELOFY_AUDIO_UPLOAD_MAXSIZE:
            raise UploadMaxSizeExceedError
        temp.write(chunk)

    return TemporaryFileType(name=temp.name, file=temp.file)
        
        
