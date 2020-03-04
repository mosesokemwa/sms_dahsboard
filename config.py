"""Flask config class."""
import os

class Config:
    """Set Flask configuration vars."""

    """Base config vars."""
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SMS_DASHBOARD_COOKIE')

     # Africa's Talking Config
    USERNAME=os.environ.get('USERNAME')
    API_KEY=os.environ.get('API_KEY')

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_DEV') or 'postgresql+psycopg2://swag:password@localhost/sms_dashboard_dev'

# class TestConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_TEST')


# class ProdConfig(Config):
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
