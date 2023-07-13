from typing import NamedTuple


class TemporaryFileType(NamedTuple):
    name: str
    content_type: str
    