"""
Django settings for MORE project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vcq8f_1#$fh4o72mr#vk8@ed$*w_7h@@l!&+_9@xryd&p!w(0w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Moremodel',
    'figure',
    'found',
    'latest',
    'mine',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.LogMiddleware.ErrorMiddleware',
]

ROOT_URLCONF = 'MORE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'MORE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'NAME': 'more',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]



LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 格式配置
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                    '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # Handler 配置
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG' if DEBUG else 'WARNING'
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '%s/logs/info.log' % BASE_DIR,  # 日志保存路径
            'when': 'D',        # 每天切割日志
            'backupCount': 30,  # 日志保留 30 天
            'formatter': 'simple',
            'level': 'INFO',
        },
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '%s/logs/error.log' % BASE_DIR,  # 日志保存路径
            'when': 'W0',      # 每周一切割日志
            'backupCount': 4,  # 日志保留 4 周
            'formatter': 'verbose',
            'level': 'WARNING',
        }
    },
    # Logger 配置
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'inf': {
            'handlers': ['info'],
            'propagate': True,
            'level': 'INFO',
        },
        'err': {
            'handlers': ['error'],
            'propagate': True,
            'level': 'WARNING',
        }
    }
}