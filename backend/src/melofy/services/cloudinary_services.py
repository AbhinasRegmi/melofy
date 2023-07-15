import os
from typing import IO, Tuple, Union

from pydantic import HttpUrl
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload_image
from cloudinary.api import delete_resources_by_tag

from melofy.utils.schemas import TemporaryFileType

class CloudinaryServices:
    @classmethod
    def upload_image(cls, image: TemporaryFileType, file_hash: str) -> str:
        """
        Provide path of the image and public url for the image is returned.
        """
   
        response = upload_image(image.name, tags=file_hash)
        url, _ = cloudinary_url(
            response.public_id,
            format=response.format
        )


        return url
    
    @classmethod
    def delete_image(cls, image_tag: str) -> None:
        delete_resources_by_tag(image_tag)
