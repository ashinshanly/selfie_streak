# noinspection PyUnresolvedReferences
from base_settings import *

ADMINS = (
    ('Muhammed K K', 'ajumell@xeoscript.com'),
    ('John Tony Thottan', 'thottanjohn@gmail.com'),
    ('Ashin Shanly', 'ashinshanly@gmail.com')
)

MANAGERS = ADMINS

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['selfiestreak.com',]

HOME_FOLDER = os.path.join('/', 'home', 'ajumell')

STATIC_ROOT = 'home/ajumell/webapps/selfiestreak_static'

STATIC_URL = '/static/'

MEDIA_ROOT =os.path.join(STATIC_ROOT,'media')
MEDIA_URL=STATIC_URL+'/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(HOME_FOLDER, 'db', 'selfiestreak_static.sqlite3'),
    }
}