from fastapi import HTTPException, status


class CredentialsInvalidError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials. Try to refresh access_token if this fails login again."
        )
    

class LoginExpiredError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login session expired. Login again."
        )

class UploadMaxSizeExceedError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Uploaded file exceeded max limit."
        )