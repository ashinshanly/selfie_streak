# coding=utf-8
# noinspection PyUnresolvedReferences
from base_settings import *

ADMINS = (
    ('Muhammed K K', 'ajumell@xeoscript.com'),
    ('John Tony Thottan', 'thottanjohn@gmail.com'),
<<<<<<< HEAD
    ('Ashin Shanly', 'ashinkoottala@gmail.com')
=======
    ('Ashin Shanly', 'ashin@gmail.com')
>>>>>>> 659e0f3b84863e77d7b53cdb048a235845dd8167
)

MANAGERS = ADMINS

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'selfiestreak.com',
    'ss.xeoscript.com',
]

HOME_FOLDER = os.path.join('/', 'home', 'ajumell')

STATIC_ROOT = '/home/ajumell/webapps/selfie_streak_static'

SITE_ID = 1


STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')

MEDIA_URL = STATIC_URL + '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(HOME_FOLDER, 'db', 'selfie-streak.sqlite3'),
    }
}
