from datetime import timedelta

from .base import *
import socket

CORS_ALLOW_ALL_ORIGINS = True

MACHINE_NAME: str = socket.gethostname()
MACHINE_IP: str = socket.gethostbyname(MACHINE_NAME)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jv&q^72-!del!fq-5=lv0w9#4md0%k6w8_n7ig!47@4zrsh8j8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [MACHINE_IP, '*']

# CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    f'http://{MACHINE_IP}',
    f'http://127.0.0.1',
]

# DEBUG TOOLS
INTERNAL_IPS = [
    # ...
    MACHINE_IP,
    '127.0.0.1'
    # ...
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


SIMPLE_JWT: dict = {
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(seconds=5),
}
