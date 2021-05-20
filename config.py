import os

class Config(object):
    SECRET__KEY = os.environ.get('SECRET_KEY') or 'oh nooooo'