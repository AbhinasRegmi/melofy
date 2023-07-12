from fastapi import HTTPException, status

class InvalidImageFormat(HTTPException):
    def __init__(self, type:  str | None) -> None:
        super().__init__(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Invalid image type provided. {type} not accepted."
        )

class InvalidAudioFormat(HTTPException):
    def __init__(self, type:  str | None) -> None:
        super().__init__(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Invalid audio type provided. {type} not accepted."
        )
        