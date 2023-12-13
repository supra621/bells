import os
from pathlib import Path

from . import env

# TODO: Factor out environment variables
#  Docker Compose convention is to use .env files in the compose.yaml root

BASE_DIR = Path(__file__).resolve().parent.parent

# TODO: Secret
with open(BASE_DIR / 'etc' / 'sk.txt', 'r') as file:
    SECRET_KEY = file.read().strip()

DEBUG = env.DEBUG

# TODO: Env
ALLOWED_HOSTS = [
    'localhost',
    'nginx',
]

ASGI_APPLICATION = 'bells.asgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.User'

# TODO: Env
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('host.docker.internal', 6379)],
        }
    }
}

# Django 4.2 states: Using a service name for testing purposes is not supported.
# This may be implemented later. https://code.djangoproject.com/ticket/33685
# TODO: Secret
with open(BASE_DIR / 'etc' / 'postgres.txt', 'r') as file:
    DATABASE_PASSWORD = file.read().strip()

# TODO: Env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'python_bells',
        'USER': 'python_bells',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': env.DATABASE_HOST,
        'PORT': env.DATABASE_PORT,
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_base',
    'accounts',
    'core',
    'chat',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

LANGUAGE_CODE = 'en-us'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bells.urls'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATIC_URL = 'static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': ['django_base.builtins'],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bells.context_processors.vite_context',
            ],
        },
    },
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

WSGI_APPLICATION = 'bells.wsgi.application'

# Additional settings

ARANGO_HOST = env.ARANGO_HOST
ARANGO_PORT = env.ARANGO_PORT
ARANGO_URL = f'{ARANGO_HOST}:{ARANGO_PORT}/'

# ARANGO_URL = 'http://arangodb:8529'

ASSET_URL = 'http://localhost:1234/assets/'

CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672'

CELERY_RESULT_BACKEND = 'redis://host.docker.internal:6379'

# TODO: Debug only
# Vite server should only run in dev/debug
VITE_CLIENT_URL = 'http://localhost:1234/assets/@vite/client'

# VITE_URL = 'http://localhost:1234/'
VITE_URL = 'assets/'
