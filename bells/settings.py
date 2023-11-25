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
            'hosts': [('127.0.0.1', 6379)],
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'var' / 'db.sqlite3',
        # Make sure tests don't run in-memory sqlite
        "TEST": {
            "NAME": BASE_DIR / 'tmp' / 'db.sqlite3'
        }
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
    'django_base',
    'accounts',
    'core',
    'chat',
]

LANGUAGE_CODE = 'en-us'

MIDDLEWARE = [
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

# STATIC_URL = 'static/'
# STATIC_URL = 'http://localhost:1234/'
STATIC_URL = 'http://localhost:1234/static/'

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

# if DEBUG:
#     import mimetypes
#     mimetypes.add_type('application/javascript', '.js', True)

# Vite server should only run in dev/debug
VITE_CLIENT_URL = 'http://localhost:1234/static/@vite/client'

VITE_URL = 'http://localhost:1234/'
