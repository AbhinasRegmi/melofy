from typing import Tuple, Generator

from gridfs import GridFS

from melofy.core.config import settings
from melofy.schemas.object_id import BaseObjectId
from melofy.utils.schemas import TemporaryFileType
from melofy.services.exceptions import MusicNotFoundError

class MongoServices:
    @classmethod
    def upload_music(cls, mdb: GridFS, file: TemporaryFileType, file_hash: str) -> BaseObjectId:
        """
        Run this as background task. Use file_hash to retrive the file.
        """
        with open(file.name, "rb") as fp:
            mongo_id = mdb.put(
                fp,
                content_type=file.content_type,
                filename=file_hash
            )

            return BaseObjectId(mongo_id=mongo_id)

    @classmethod
    def stream_music(cls, mdb: GridFS, file_hash: str) -> Tuple[str, Generator[bytes, None, None]]:
        """
        Returns the content-type of the stream, and stream function to consume.
        """
        #todo: streaming controls.
        file = mdb.find_one({"filename": file_hash})

        if not file:
            raise MusicNotFoundError
        
        content_type: str = file.content_type #type:ignore content_type is uploaded during file upload

        def streamer() -> Generator[bytes, None, None]:
            while chunk:=file.read(settings.MELOFY_STREAMING_SIZE):
                yield chunk

        return content_type, streamer()
