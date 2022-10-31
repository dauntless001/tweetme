from tweetme.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l3*e-3+yas_99_-^k+5-625iy@8fb(izprubz%^_zy&$s)jpvn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'tweetme.db',
}