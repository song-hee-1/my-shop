from config.settings.base import *
from config.settings.secrets import get_secrets

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secrets('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
