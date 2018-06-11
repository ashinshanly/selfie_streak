# noinspection PyUnresolvedReferences
from base_settings import *
"""
INSTALLED_APPS += (
    'django_generators',
)
"""
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root")

MEDIA_URL='/media/'

ALLOWED_HOSTS = ["*"]