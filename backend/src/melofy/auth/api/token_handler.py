from fastapi import APIRouter, Query

from melofy.schemas.token_schema import Token
from melofy.core.auth_tokens import exchange_auth_tokens

token_handler = APIRouter(
    prefix="/token"
)

@token_handler.get("/exchange")
def exchange_for_access(refresh_token: str = Query(...)) -> Token:
    """
    Exchange your refresh_token to get new access_token.
    """
    return exchange_auth_tokens(refresh_token)
