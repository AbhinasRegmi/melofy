from typing import NamedTuple, IO


class TemporaryFileType(NamedTuple):
    name: str
    file: IO