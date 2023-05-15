import os
from distutils.util import strtobool

from dotenv import load_dotenv

# Load env var from dotenv file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
env_path = os.path.join(APP_ROOT, '.env')
load_dotenv(env_path)

DEBUG = True

FLASK_APP_VERSION = os.getenv('FLASK_APP_VERSION')

SECRET_KEY = os.getenv('SECRET_KEY')
SERVER_NAME = os.getenv('SERVER_NAME', 'localhost:8000')

# Flask-Mail.
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = int(os.getenv('MAIL_PORT'))
MAIL_USE_TLS = bool(strtobool(os.getenv('MAIL_USE_TLS', 'true')))
MAIL_USE_SSL = bool(strtobool(os.getenv('MAIL_USE_SSL', 'false')))
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

CLIENT_APP_URL = os.getenv('CLIENT_APP_URL')

# SQLAlchemy.
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', '')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Apispec config
DOC_TITLE = os.getenv('DOC_TITLE')
DOC_VERSION = os.getenv('DOC_VERSION')
DOC_OPEN_API_VERSION = os.getenv('DOC_OPEN_API_VERSION', '3.0.2')

TIMEZONE = os.getenv('TIMEZONE', 'Asia/Tokyo')


# iPalet DB connection information
iPALET_DB_IP = os.getenv('iPALET_DB_IP', '')
iPALET_DB_USER = os.getenv('iPALET_DB_USER', '')
iPALET_DB_PASSWORD = os.getenv('iPALET_DB_PASSWORD', '')
iPALET_DB_NAME = os.getenv('iPALET_DB_NAME', '')

DOCUMENT_DRIVE_ROOT = os.getenv('DOCUMENT_DRIVE_ROOT', os.path.join(APP_ROOT, 'document_drive'))
DATA_EXPORT_DIR = os.path.join(APP_ROOT, 'exports')

IMAGE_DRIVE_ROOT = os.getenv('IMAGE_DRIVE_ROOT')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
ACCESS_TOKEN_EXPIRES_IN = int(
    os.getenv('ACCESS_TOKEN_EXPIRES_IN', 10))  # in minutes
REFRESH_TOKEN_EXPIRES_IN = int(
    os.getenv('REFRESH_TOKEN_EXPIRES_IN', 5))  # in days
