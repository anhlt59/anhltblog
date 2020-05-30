"""
Django settings for graph project.
"""

import environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = (environ.Path(__file__) - 3)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party apps
    "graphene_django",
    "django_filters",
    "crispy_forms",
    "guardian",
    # installed apps
    "graphql_api",
    "core",
    "blog",
    "users",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES_DIR = BASE_DIR('templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR('db.sqlite3'),
#     }
# }

# Password validation
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


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

AUTH_USER_MODEL = 'auth.User' # default django.contrib.auth.User
LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = '/users/login'

# datetime format
DATE_INPUT_FORMATS = ['%d-%m-%Y']

WSGI_APPLICATION = 'config.wsgi.application'
# ASGI_APPLICATION = 'config.asgi.application'

# graphene_django
GRAPHENE = {
    "SCHEMA": "graphql_api.schema.schema",
    # "SCHEMA_OUTPUT": "data/myschema.json",
    # "MIDDLEWARE": [
    #     "graphql_jwt.middleware.JSONWebTokenMiddleware",
    # ]
}

# # graphql jwt
# from datetime import timedelta
# GRAPHQL_JWT = {
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
#     'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
# }
#
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
#     'graphql_jwt.backends.JSONWebTokenBackend',
#     'django.contrib.auth.backends.ModelBackend',
)
# # config logging
import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'all': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "%(asctime)s",
                "%(name)s:%(lineno)s",
                "%(message)s",
            ])
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'all',
            'stream': sys.stdout,
        },
        # 'info': {
        #     'level': 'INFO',
        #     'class': 'watchtower.CloudWatchLogHandler',
        #     'boto3_session': boto3_session,
        #     'log_group': 'CloudWatch-Log-Django-App',
        #     'stream_name': LOG_STREAM,
        #     'formatter': 'all',
        # },
        # 'error': {
        #     'level': 'ERROR',
        #     'class': 'watchtower.CloudWatchLogHandler',
        #     'boto3_session': boto3_session,
        #     'log_group': 'CloudWatch-Log-Django-App',
        #     'stream_name': LOG_STREAM,
        #     'formatter': 'all',
        # },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'app': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        # 'cloudwatch': {
        #     'handlers': ['info', 'error'],
        #     'level': 'INFO',
        #     'propagate': True,
        # },
    },
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# migrations module
MIGRATION_MODULES = {
    "blog": "core.migrations.blog",
    "users": "core.migrations.users",
}

# from django.contrib.messages import constants as messages
#
# MESSAGE_TAGS = {
#     messages.DEBUG: 'alert-info',
#     messages.INFO: 'alert-info',
#     messages.SUCCESS: 'alert-success',
#     messages.WARNING: 'alert-warning',
#     messages.ERROR: 'alert-danger',
# }