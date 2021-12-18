import os

from NoteTrading.settings import BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/static/'),
    os.path.join(BASE_DIR, '/bonus/static/')
)
