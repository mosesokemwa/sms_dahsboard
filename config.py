"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    """Base config vars."""
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SMS_DASHBOARD_COOKIE')

     # Africa's Talking Config
    USERNAME=os.environ.get('USERNAME')
    API_KEY=os.environ.get('API_KEY')

# class ProdConfig(Config):
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


# class DevConfig(Config):
#     DEBUG = True
#     TESTING = True
#     DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

#     # General Config
