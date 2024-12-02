import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '12345678')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:@localhost/app_server')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
