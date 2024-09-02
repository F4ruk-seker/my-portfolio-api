from datetime import timedelta

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')
CSRF_TRUSTED_ORIGINS = [
    f"https://{env('PRODUCT_HOST')}/",
    f"https://{env('PRODUCT_API_HOST')}",
    f"https://{env('FEATURE_PRODUCT_HOST')}"
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [env('PRODUCT_HOST'), env('PRODUCT_API_HOST'), env('FEATURE_PRODUCT_HOST')]

for _ in ALLOWED_HOSTS:
    CUSTOM_LOGGER.construct(
        title="HOSTs",
        description="info",
        level="info",
        metadata={
            "Metrics": {
                "host": _,
            },
        },
    )
    CUSTOM_LOGGER.send()


for _ in CSRF_TRUSTED_ORIGINS:
    CUSTOM_LOGGER.construct(
        title="CSRF HOSTs",
        description="info",
        level="info",
        metadata={
            "Metrics": {
                "host": _,
            },
        },
    )
    CUSTOM_LOGGER.send()


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': env('PGPORT')
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

CORS_ALLOW_ALL_ORIGINS = True  # temp for server settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles/'

SIMPLE_JWT: dict = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
}
