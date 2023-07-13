from typing import AsyncGenerator, Any

from gridfs import GridFS
from melofy.utils.schemas import TemporaryFileType


class MongoServices:
    @classmethod
    def upload_music(cls, mdb: GridFS, file: TemporaryFileType, file_hash: str) -> Any:
        with open(file.name) as fp:
            oid = mdb.put(
                fp,
                content_type=file.content_type,
                filename=file_hash
            )

            return oid
    @classmethod
    async def stream_music(cls, file_hash: str) -> AsyncGenerator[bytes, None]:
        ...