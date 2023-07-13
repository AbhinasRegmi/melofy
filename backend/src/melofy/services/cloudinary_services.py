import os
from uuid import uuid4
from typing import IO, Tuple, Union

from pydantic import HttpUrl
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload_image
from cloudinary.api import delete_resources_by_tag

from melofy.utils.schemas import TemporaryFileType

class CloudinaryServices:
    @classmethod
    def upload_image(cls, image: TemporaryFileType) -> Tuple[HttpUrl, str]:
        """
        Provide path of the image and public url for the image is returned.
        """
    
        tag=str(uuid4())
        response = upload_image(image.name, tags=tag)
        url, _ = cloudinary_url(
            response.public_id,
            format=response.format
        )


        return HttpUrl(url), tag
    
    @classmethod
    def delete_image(cls, image_tag: str) -> None:
        delete_resources_by_tag(image_tag)
