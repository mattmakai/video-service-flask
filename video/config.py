import os

SECRET_KEY = os.environ.get('SECRET_KEY', '')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', '')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
