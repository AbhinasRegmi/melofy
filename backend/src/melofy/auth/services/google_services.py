import httpx

from melofy.core.config import settings

class GoogleServices:
    @classmethod
    async def get_google_consent_form(cls) -> str:
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

