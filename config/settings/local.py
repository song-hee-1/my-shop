from config.settings.base import *
from config.settings.secrets import get_secrets

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = get_secrets('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secrets('DATABASE_NAME'),
        'USER': get_secrets('DATABASE_USER'),
        'PASSWORD': get_secrets('DATABASE_PASSWORD'),
        'HOST': get_secrets('DATABASE_HOST'),
        'PORT': get_secrets('DATABASE_PORT'),
    }
}
