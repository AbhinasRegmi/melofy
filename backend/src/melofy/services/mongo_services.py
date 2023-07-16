from typing import Generator, Any

import aiofiles
from gridfs import GridFS

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
    def stream_music(cls, mdb: GridFS, file_hash: str) -> Generator[bytes, None, None]:
        file = mdb.find_one({"filename": file_hash})

        if not file:
            raise MusicNotFoundError

        for chunk in file.readchunk():
            yield chunk

    @classmethod
    async def test_stream(cls, mdb: GridFS, file_hash: str) -> Generator[bytes, None, None]:
        async with aiofiles.open("./song.MP4", mode='rb') as handler:
            yield from handler
