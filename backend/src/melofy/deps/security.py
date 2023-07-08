from typing import Optional

from sqlalchemy.orm import Session
from fastapi import Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from melofy.deps.database import get_db
from melofy.models.user_model import User
from melofy.schemas.token_schema import JWTTokenData
from melofy.core.auth_tokens import validate_auth_tokens
from melofy.services.user_services import UserServices
from melofy.deps.exceptions import UserNotFoundError, NotAuthenticatedError


class AccessTokenBearer(HTTPBearer):
    async def __call__(self, request: Request) -> str:
        """
        Only return the auth_token leave out the scheme
        """
        http_auth_credentials: Optional[HTTPAuthorizationCredentials]  = await super().__call__(request)

        if not http_auth_credentials:
            raise NotAuthenticatedError
        
        return http_auth_credentials.credentials
        

oauth2_scheme = AccessTokenBearer(
    scheme_name="access_token",
    description="Get your tokens from `/api/v1/auth/google/login`"
)

def login_required(token: str = Depends(oauth2_scheme)) -> JWTTokenData:
    """
    Use this if the user only has to be logged in. No database call Required.
    """
    return validate_auth_tokens(token)

def get_current_user(db: Session = Depends(get_db), token_data: JWTTokenData = Depends(login_required)) -> User:
    
    user_db = UserServices.get_user_by_email(db, token_data.sub)

    if not user_db:
        raise UserNotFoundError
    
    return user_db

