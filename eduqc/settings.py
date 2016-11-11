"""
Django settings for eduqc project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_y!x0hrsuto^u%5o)3hc8y7lqweri&abnf3(0f*og(4pj__ie1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'password_reset',
    'custom_user',
    'django_markdown',

    'courses',
    'emails',
    'index',
    'payments',
    'users',
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

ROOT_URLCONF = 'eduqc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'eduqc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eduqc',
        'USER': 'eduqc',
        'PASSWORD': 'eduqc',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')


# Costum User
AUTH_USER_MODEL = 'users.User'


# Where to redirect when an anonymous user tries to access a login_required page
# We redirect to the root url because our landing page is also our login page
LOGIN_URL = '/'

# Print emails to terminal instead of trying to actually send them:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATE_INPUT_FORMATS = ('%d/%m/%Y',)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'director@quantcompany.com'
EMAIL_HOST_PASSWORD = 'quant_zx_963'
DEFAULT_FROM_EMAIL = 'Quant Company <do-not-reply@quantcompany.com>'
EMAIL_PORT = 587

#EMAIL_PORT = 465
#EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
#EMAIL_USE_SSL = True
#EMAIL_HOST = 'smtp.zoho.com'
#EMAIL_HOST_USER = 'info@tripletherapy.net'
#EMAIL_HOST_PASSWORD = 'quant_zx_963'
#DEFAULT_FROM_EMAIL = 'info@tripletherapy.net'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

COURSES_PER_PAGE = 3

try:
    from local_settings import *
except:
    pass
