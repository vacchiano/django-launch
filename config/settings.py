"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7zarf57(_&o0dn1&y+(_1pbrd(l(1ji$g+8(($*4lrywjzy9id'

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
    "django.contrib.sites", #all-auth

    #3rd party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",

    #local apps
    "accounts",
    "pages",
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS":[str(BASE_DIR.joinpath("templates"))],
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


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #changed from sqlite
        'NAME': 'postgres', #development settings, will change in production
        'USER': 'postgres', #development settings, will change in production
        'PASSWORD': 'postgres', #development settings, will change in production
        'HOST': 'db',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles')) #for production
STATICFILES_FINDERS = [ "django.contrib.staticfiles.finders.FileSystemFinder", "django.contrib.staticfiles.finders.AppDirectoriesFinder", ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# all auth settings

SITE_ID = 1     #all-auth supports multiple sites

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend", #this how admins will log in to the admin site
    "allauth.account.auth_backends.AuthenticationBackend", #this how users log in
]
LOGIN_REDIRECT_URL = "home"   #change to desired url name
LOGOUT_REDIRECT_URL = "home" #change to desired url name
ACCOUNT_SESSION_REMEMBER = True #remember user via sessions
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False #preferred UX
ACCOUNT_USERNAME_REQUIRED = False #preferred UX
ACCOUNT_AUTHENTICATION_METHOD = "email" 
ACCOUNT_EMAIL_REQUIRED = True #required for email authentication
ACCOUNT_UNIQUE_EMAIL = True #required for email authentication
ACCOUNT_EMAIL_VERIFICATION = "optional" #can use as a welcome email as well
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
AUTH_USER_MODEL = "accounts.CustomUser"

# email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" 

#django crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'