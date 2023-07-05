import httpx
from pydantic import ValidationError

from melofy.core.config import settings
from melofy.auth.schemas.google_response import GoogleTokenResponse
from melofy.auth.services.exceptions import GoogleTokenResponseError

class GoogleServices:
    @classmethod
    def get_google_consent_form(cls) -> str:
        """
        Get a link for the google consent form.
        """
        HEADERS = {"Accept": "application/json"}
        PARAMS = {
            "redirect_uri": settings.GOOGLE_CALLBACK_URL,
            "client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            "access_type": "offline",
            "response_type": "code",
            "prompt": "consent",
            "scope": " ".join([
                settings.GOOGLE_USER_EMAIL_SCOPE_URL,
                settings.GOOGLE_USER_PROFILE_SCOPE_URL
            ])
        }

        consent_url = httpx.Client().build_request(
            method='GET',
            url=settings.GOOGLE_OAUTH_ROOT_URL,
            headers=HEADERS,
            params=PARAMS
        ).url

        return str(consent_url)

    @classmethod
    async def get_google_token(cls, code: str) -> GoogleTokenResponse:
        """
        Use the code to acquire access_token and id_token from google
        """
        HEADERS = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        PARAMS = {
            "code": code,
            "client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            "client_secret": settings.GOOGLE_OAUTH_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_CALLBACK_URL,
            "grant_type": "authorization_code"
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=settings.GOOGLE_OAUTH_TOKEN_URL,
                    headers=HEADERS,
                    params=PARAMS
                )

                response_json = response.json()

                return GoogleTokenResponse(
                    **response_json
                )
        except ValidationError:
            raise GoogleTokenResponseError