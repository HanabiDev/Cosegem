"""
Django settings for Cosegem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lm+3)v-j2-gq1bwv*9blq+_8qf@px5x$_#d)zu3i6=lvt+bb0m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


import socket
if socket.gethostname().startswith('localhost'):
    DEVEL = True
else:
    DEVEL = False

DEBUG = True

TEMPLATE_DEBUG = DEVEL

if DEVEL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'periodic_nuevo',
            'USER': 'periodic_nuevoad',
            'PASSWORD': 'cotpbmcg',
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'user_sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'ursus_auth',
    #'ursus',
)

MIDDLEWARE_CLASSES = (
    'user_sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SESSION_ENGINE = 'user_sessions.backends.db'

ROOT_URLCONF = 'Cosegem.urls'

WSGI_APPLICATION = 'Cosegem.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Override Login and Logout URLs
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('ursus_auth:account')
LOGOUT_URL = reverse_lazy('ursus_auth:logout')


#GeoIP database binaries
GEOIP_PATH = os.path.join(BASE_DIR, 'GeoIP_DB')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'ursus/templates/'),
)
