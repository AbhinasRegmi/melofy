from fastapi import status, HTTPException


class GoogleTokenResponseError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login expired. Try to login again."
        )

class InvalidAccessOrIdTokenError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials. Try and login in again."
        )

class MusicNotFoundError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such music found."
        )