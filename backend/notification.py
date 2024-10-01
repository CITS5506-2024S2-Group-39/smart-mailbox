import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

def send_email_notification(to_email, subject, content):
    message = Mail(
        from_email='your_email@example.com',
        to_emails=to_email,
        subject=subject,
        html_content=content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f'Email sent: {response.status_code}')
        return response.status_code == 202
    except Exception as e:
        print(f'Error sending email: {e}')
        return False

def send_sms_notification(to_phone, message_body):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
        print(f'SMS sent: {message.sid}')
        return True
    except Exception as e:
        print(f'Error sending SMS: {e}')
        return False
