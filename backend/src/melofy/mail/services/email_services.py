import ssl
import smtplib
from typing import Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from jinja2 import Template #type:ignore
from pydantic import EmailStr

from melofy.core.config import settings

class EmailService:
    @classmethod
    def send_mail_to_client(
        cls,
        send_to: EmailStr,
        template: Template,
        context: dict,
        subject: Optional[str] = None ) -> None:
        """
        This is has to be a background task to send email.
        """

        ssl_context = ssl.create_default_context()
        rendered_mail = template.render(context)
        body = MIMEText(rendered_mail, 'html')
        
        message = MIMEMultipart()

        if subject:
            message['Subject'] = subject
        message['From'] = settings.MELOFY_SMTP_LOGIN
        message['To'] = send_to
        message.attach(payload=body)

        with smtplib.SMTP_SSL(
            host=settings.GOOGLE_SMTP_HOST,
            port=settings.GOOGLE_SMTP_PORT,
            context=ssl_context) as server:

            server.login(
                user=settings.GOOGLE_SMTP_LOGIN,
                password=settings.GOOGLE_SMTP_PASS
            )

            server.sendmail(
                settings.MELOFY_SMTP_LOGIN,
                to_addrs=send_to,
                msg=message.as_string()
            )

