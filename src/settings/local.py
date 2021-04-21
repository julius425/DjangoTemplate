from .base import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS += [

    # debug
    'django_extensions',
    'debug_toolbar',
    'flower',

]

pass
try:
    from .local import *
except ImportError:
    pass