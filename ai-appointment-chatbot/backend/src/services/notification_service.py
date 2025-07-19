from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

class NotificationService:
    def __init__(self):
        self.twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        self.sendgrid_client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))

    def send_sms(self, to, message):
        try:
            message = self.twilio_client.messages.create(
                body=message,
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                to=to
            )
            return message.sid
        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return None

    def send_email(self, to, subject, content):
        message = Mail(
            from_email=os.getenv('SENDGRID_FROM_EMAIL'),
            to_emails=to,
            subject=subject,
            plain_text_content=content
        )
        try:
            response = self.sendgrid_client.send(message)
            return response.status_code
        except Exception as e:
            print(f"Failed to send email: {e}")
            return None

    def send_reminder(self, to, appointment_details):
        subject = "Appointment Reminder"
        content = f"Reminder: You have an appointment scheduled for {appointment_details}."
        self.send_email(to, subject, content)
        self.send_sms(to, content)