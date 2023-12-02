from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


with open(BASE_DIR / 'etc' / 'sk.txt', 'r') as file:
    SECRET_KEY = file.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ###

ALLOWED_HOSTS = []

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

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        }
    }
}

# Django 4.2 states: Using a service name for testing purposes is not supported.
# This may be implemented later. https://code.djangoproject.com/ticket/33685
with open(BASE_DIR / 'etc' / 'db.txt', 'r') as file:
    DB_PASSWORD = file.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'python_bells',
        'USER': 'python_bells_owner',    # env
        'PASSWORD': DB_PASSWORD,         # env
        # 'HOST': '127.0.0.1',           # env, if running from system
        'HOST': 'host.docker.internal',  # env, if using docker
        'PORT': '5432',                  # env
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

STATICFILES_DIRS = ['static']

STATIC_URL = 'static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
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

GREMLIN_URL = 'ws://localhost:8182/gremlin'

# Vite server should only run in dev/debug
VITE_CLIENT_URL = 'http://localhost:1234/@vite/client'

VITE_URL = 'http://localhost:1234/'
