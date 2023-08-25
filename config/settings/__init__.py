import os

if os.environ.get('ENV_SETTINGS_MODE') is None:
    ENV_MODE = 'local'
elif os.environ.get('ENV_SETTINGS_MODE') == 'prod':
    ENV_MODE = 'prod'
elif 'devel' in os.environ.get('ENV_SETTINGS_MODE'):
    ENV_MODE = 'devel'
else:
    ENV_MODE = 'local'

if ENV_MODE == 'prod':
    from config.settings.prod import *
elif ENV_MODE == 'devel':
    from config.settings.devel import *
elif ENV_MODE == 'local':
    from config.settings.local import *

