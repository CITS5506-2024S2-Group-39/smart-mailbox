import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import get_setting_item
from config import EmailConfig
from shared import ISODateTime


def send_email_notification(type: str, time: str, data: dict, id: int):
    receipient = get_setting_item("notification.email", None)
    if not receipient:
        return

    # Parse the time string as a UTC datetime object
    time = ISODateTime.from_string(time)
    # Convert the UTC time to the local timezone
    # TODO: Respect user's regional timezone settings
    time = time.astimezone()
    time = time.strftime("%B %d, %Y %H:%M:%S")
    subject = f"[Smart Mailbox] {type}"

    content = [
        f"""<p><strong>Summary:</strong> {data['summary']}</p>""",
        f"""<p><strong>Time:</strong> {time}</p>""",
        f"""<p>For details, please visit the <a href="http://{EmailConfig.HOST_NAME}/event/{id}">dashboard</a>.</p>""",
    ]

    if "image" in data:
        line = f"""<img src="http://{EmailConfig.HOST_NAME}/api/images/{data['image']}" />"""
        content.insert(0, line)

    msg = MIMEText("\n".join(content), "html")
    msg["From"] = EmailConfig.EMAIL_USER
    msg["To"] = receipient
    msg["Subject"] = subject

    with smtplib.SMTP_SSL(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT) as server:
        server.login(EmailConfig.EMAIL_USER, EmailConfig.EMAIL_PASSWORD)
        server.send_message(msg)
