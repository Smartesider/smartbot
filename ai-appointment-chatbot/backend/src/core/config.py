from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", "False") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    GOOGLE_CALENDAR_API_KEY = os.getenv("GOOGLE_CALENDAR_API_KEY", "your_google_calendar_api_key")
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "your_sendgrid_api_key")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_twilio_account_sid")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_twilio_auth_token")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")