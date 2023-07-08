from fastapi import APIRouter
from fastapi import Query, Depends
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from fastapi.responses import RedirectResponse

from melofy.deps.database import get_db
from melofy.core.auth_tokens import get_auth_tokens
from melofy.schemas.token_schema import JWTTokenData
from melofy.db.services.user_services import UserServices
from melofy.db.schemas.user_schema import UserCreateSchema
from melofy.mail.schemas.template_schema import HTMLTemplate
from melofy.mail.services.email_services import EmailService
from melofy.auth.services.google_services import GoogleServices

google_handler = APIRouter(
    prefix='/google'
)


@google_handler.get("/login", response_class=RedirectResponse)
async def get_login_form():
    """
    Get the google login form or consent form and get your tokens.
    """
    return RedirectResponse(
        url=GoogleServices.get_google_consent_form()
    )


@google_handler.get("/callback")
async def google_callback(background: BackgroundTasks, db: Session = Depends(get_db), code: str = Query(...)):
    """
    Do not call this end-point directly. You should be redirected here automatically with
    appropriate headers.
    """
    response = await GoogleServices.get_google_token(code)
    user_detail = await GoogleServices.get_user_detail(response)

    if not (user:=UserServices.get_user_by_email(db, user_detail.email)):
        user_in = UserCreateSchema(
            email=user_detail.email,
            avatar=user_detail.avatar,
            is_verified=user_detail.verified
        )

        UserServices.create_user(db, user_in)
        background.add_task(
            EmailService.send_mail_to_client,
            send_to=user_detail.email,
            template=HTMLTemplate.WELCOME,
            context={})
    
    auth_token = get_auth_tokens(
        data=JWTTokenData(sub=user_detail.email)
    )

    return auth_token