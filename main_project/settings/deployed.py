from .base_settings import *

import dj_database_url
import os

DEBUG = os.environ.get("DEBUG") == 'True'

ALLOWED_HOSTS = [
    'protect-cloud-bread.apps.all-co.de',
]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
