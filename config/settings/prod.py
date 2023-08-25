from config.settings.base import *
from config.settings.secrets import get_secrets

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = get_secrets('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False