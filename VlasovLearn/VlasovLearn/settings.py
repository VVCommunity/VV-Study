"""
Django settings for VlasovLearn project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '307038e3-095e-4a88-90c5-62b0b9782c47'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['www.vvcommunity.ru','vvcommunity.ru','localhost']

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [ 
    # Add your apps here to enable them
    'channels',
    'google_analytics', 
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'Accaunt',
    'LearnSystem',
    'BlogSystem',
    'googlecharts',
    'TapLinkByVlasov', 
    'qsstats', 
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VlasovLearn.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', # Добавил эту строку
            ],
        },
    },
]
SOCIAL_AUTH_VK_OAUTH2_KEY = '7421383'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'XNK6MgzNvnastRP5zjcx'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email'] 
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '152201056874-8b74beodsetrd58f18043treni02bvit.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'biFhoYJ9rYkzAzZuUyDOqZFg'
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.associate_by_email',
)
LOGIN_REDIRECT_URL = '/'
WSGI_APPLICATION = 'VlasovLearn.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',          # бекенд авторизации через ВКонтакте
    'django.contrib.auth.backends.ModelBackend', 
    'social_core.backends.google.GoogleOAuth2', # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
)
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

MEDIA_URL = '/media/'
MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media']))

ASGI_APPLICATION = 'VlasovLearn.asgi.application' 
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
  
# почты для получения писем
# почта отправителя по умолчанию, та что верифицирована
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'                                                                           
EMAIL_HOST ='mail.vvcommunity.ru'                                   
EMAIL_PORT = 587                                                             
EMAIL_HOST_USER = 'support@vvcommunity.ru'                              
EMAIL_HOST_PASSWORD = 'zb!UWF8W' #This is not your gmail password.
EMAIL_USE_TLS = True

GOOGLE_ANALYTICS_MODEL = True
GOOGLE_ANALYTICS = {
    'google_analytics_id': 'UA-187658591-1',
}