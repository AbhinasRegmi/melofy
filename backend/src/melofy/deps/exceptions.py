from fastapi import HTTPException, status


class UserNotFoundError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found. Try to Login again."
        )

class NotAuthenticatedError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authenticated"
        )