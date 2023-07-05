from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

from melofy.auth.services.google_services import GoogleServices


google_handler = APIRouter(
    prefix='/google'
)


@google_handler.get("/login", response_class=RedirectResponse)
async def get_login_form():
    """
    Get the google login form or consent form.
    """
    return RedirectResponse(
        url=GoogleServices.get_google_consent_form()
    )


@google_handler.get("/callback")
async def google_callback(code: str = Query(...)):
    response = await GoogleServices.get_google_token(code)
    
    return response