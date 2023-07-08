from melofy.schemas.token_schema import Token, JWTTokenData
from melofy.utils.tokens import validate_access_token, validate_refresh_token
from melofy.utils.tokens import generate_jwt_access_token, generate_jwt_refresh_token

def get_auth_tokens(data: JWTTokenData) -> Token:
    access_token = generate_jwt_access_token(data)
    refresh_token = generate_jwt_refresh_token(data)

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )

def validate_auth_tokens(token: Token) -> JWTTokenData:
    # we will only validate access_token and send data
    return validate_access_token(access_token=token.access_token)

def exchange_auth_tokens(token: Token) -> Token:
    # we will verify refresh_token and provide new access_token
    # when refresh_token expires need to login again
    data = validate_refresh_token(refresh_token=token.refresh_token)
    access_token = generate_jwt_access_token(data=data)
    
    return Token(
        access_token=access_token,
        refresh_token=token.refresh_token,
        token_type="Bearer"
    )