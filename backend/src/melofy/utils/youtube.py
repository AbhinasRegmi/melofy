"""
Download audio from youtube.
"""
import os
from contextlib import contextmanager

from pytube import YouTube

from melofy.schemas.upload_schema import AudioType
from melofy.utils.schemas import TemporaryFileType


class GetMusicFromYoutube:
    def __init__(self, music_url: str) -> None:
        self._music_url = music_url
        self._yobj = YouTube(self._music_url)
        self._file = None

    def __enter__(self) -> TemporaryFileType:
        ystream = self._yobj.streams.filter(only_audio=True, mime_type=AudioType.mp4)

        if ystream:
            ystream = ystream[0]
        else:
            raise ValueError(f"Couldn't find mp4 audio for {self._music_url}")
        
        outfile = ystream.download(output_path='.')
        base, ext = os.path.split(outfile)
        newfile = base +  '.mp4'
        os.rename(outfile, newfile)

        self._file = newfile

        return TemporaryFileType(name=self._file, content_type=AudioType.mp4)
    
    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        if self._file:
            os.remove(self._file)
            pass