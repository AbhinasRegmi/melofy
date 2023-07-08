"""
All jwt token generation and validation.
"""
from datetime import datetime, timedelta

from jose import JWTError, jwt
from pydantic import ValidationError

from melofy.core.config import settings
from melofy.schemas.token_schema import JWTTokenData
from melofy.utils.exceptions import CredentialsInvalidError, LoginExpiredError

def generate_jwt_access_token(data: JWTTokenData) -> str:
    to_encode = data.dict().copy()
    to_encode.update(
        {
            "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXP)
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_ACCESS_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt

def generate_jwt_refresh_token(data: JWTTokenData) -> str:
    to_encode = data.dict().copy()
    to_encode.update(
        {
            "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_REFRESH_TOKEN_EXP)
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_REFRESH_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt


def validate_access_token(access_token: str) -> JWTTokenData:
    try:
        payload = jwt.decode(
            access_token,
            settings.JWT_ACCESS_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return JWTTokenData(**payload)
    except (ValidationError, JWTError):
        raise CredentialsInvalidError
    
def validate_refresh_token(refresh_token: str) -> JWTTokenData:
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return JWTTokenData(**payload)
    except (ValidationError, JWTError):
        raise LoginExpiredError