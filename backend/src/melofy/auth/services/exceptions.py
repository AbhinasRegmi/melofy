from fastapi import status, HTTPException


class GoogleTokenResponseError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login expired. Try to login again."
        )