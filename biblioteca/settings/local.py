from .base import *

DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'neunapp',
        'PASSWORD': 'neunapp2020',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
