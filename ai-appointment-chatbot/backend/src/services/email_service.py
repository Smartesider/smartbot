from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

class EmailService:
    def __init__(self):
        self.sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    def send_email(self, to_email, subject, content):
        message = Mail(
            from_email=os.environ.get('FROM_EMAIL'),
            to_emails=to_email,
            subject=subject,
            html_content=content
        )
        try:
            response = self.sendgrid_client.send(message)
            return response.status_code, response.body, response.headers
        except Exception as e:
            print(f"Error sending email: {e}")
            return None

    def parse_incoming_email(self, email_data):
        # Logic to parse incoming email data
        pass

    # Additional email-related functionalities can be added here.