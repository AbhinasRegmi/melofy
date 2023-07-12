from pathlib import Path

import cloudinary
import cloudinary.api
from pydantic import HttpUrl
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload_image

from melofy.core.config  import settings


class CloudinaryServices:
    @classmethod
    def upload_image(cls, image_path: Path) -> HttpUrl:
        """
        Provide path of the image and public url for the image is returned.
        """
        response = upload_image(image_path)
        url, _ = cloudinary_url(
            response.public_id,
            format=response.format
        )

        return HttpUrl(url)
