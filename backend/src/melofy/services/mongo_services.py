from typing import AsyncGenerator

from melofy.utils.schemas import TemporaryFileType


class MongoServices:
    @classmethod
    async def upload_music(cls, mdb, file: TemporaryFileType, file_hash: str) -> None:
        grid_in = mdb.open_upload_stream(
            hash,
            metadata={'ContentType': file.content_type}
        )

        with open(file.name) as fp:
            data = fp.read()

        await grid_in.write(data)
        await grid_in.close()

    @classmethod
    async def stream_music(cls, file_hash: str) -> AsyncGenerator[bytes, None]:
        ...