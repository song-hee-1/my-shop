from config.settings.secrets import get_secrets
from config.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = get_secrets('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True