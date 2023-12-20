
import os
import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api
env = environ.Env()
environ.Env.read_env()
from pathlib import Path
import dj_database_url

import mimetypes
mimetypes.add_type("text/css", ".css", True)

SECRET_KEY =os.environ.get('SECRET_KEY')
DEBUG =os.environ.get('DEBUG')
ALLOWED_HOSTS =list[os.environ.get['ALLOWED_HOSTS']]
# DEBUG = True
# ALLOWED_HOSTS = ['*']
BASE_DIR = Path(__file__).resolve().parent.parent
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
    'storages',
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_tailwind", 
    'tailwind',
    'theme',
    'django_browser_reload',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    'ckeditor_uploader',
    'ckeditor',
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    'django_filters',
    'widget_tweaks',
    'cloudinary',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

LOCAL_APPS = [
    "content",
    "users",
    'core',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

NOTIFY_EMAIL =os.environ.get('NOTIFY_EMAIL')
DEFAULT_FROM_EMAIL =os.environ.get('DEFAULT_FROM_EMAIL')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'config.urls'
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
WSGI_APPLICATION = 'config.wsgi.application'
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': BASE_DIR / 'db.sqlite3',
#      }
#  }
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
USE_THOUSAND_SEPARATOR = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1


LOGIN_REDIRECT_URL = "content:course-list"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

DJANGO_WYSIWYG_FLAVOR = "ckeditor"


CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BROWSE_SHOW_DIRS = True 
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'height':100,
    },
    
}

AUTH_USER_MODEL = 'users.User'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
SITE_ID = 1


CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
TAILWIND_APP_NAME = 'theme'
CRISPY_TEMPLATE_PACK = "tailwind"
CRISPY_CLASS_CONVERTERS = {
    'textinput': 'dark:text-white text-gray-700'
}

cloudinary.config( 
  cloud_name =os.environ.get('cloud_name_KEY'), 
  api_key =os.environ.get('api_key_KEY'),
  api_secret =os.environ.get('api_secret_KEY')
)

# NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
NPM_BIN_PATH = r"C:/Program Files/nodejs/npm.cmd"

