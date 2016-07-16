# Local configuration file
# Adjust as you need

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'am+mtwaazf9uxu@x#2x396!1oey(+g)usvapj4g#v%-l)y2(hc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Emailsettings
DEFAULT_FROM_EMAIL = 'partuniverse@example.com'

# Temp. no real mail sending out
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{component.database.database}}',
        'USER': '{{component.database.username}}',
        'PASSWORD': '{{component.database.password}}',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


MEDIA_URL = 'http://localhost:8000/img/'
