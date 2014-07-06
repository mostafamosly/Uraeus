"""
Django settings for Small project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7!7o^g+4-v%im@@+9l815_1+y!390chlo)te*i*ws2dr^gtdr*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django_admin_bootstrapped.bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djangobower',
    'django_nvd3',
    'crispy_forms',
    'bootstrap3',
    'procurement',
    'core',
    'product',
    'accounting',
    'warehouse',
    #'purchase',
    'fulfillment',
    'registration',
    # 'shop',
    'djangobower',
)

#CRISPY_TEMPLATE_PACK = 'bootstrap3'

ACCOUNT_ACTIVATION_DAYS = 7

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Small.urls'

WSGI_APPLICATION = 'Small.wsgi.application'


GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]





STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder', 'djangobower.finders.BowerFinder',
)

BOWER_INSTALLED_APPS = (
    'nvd3',
    'd3',
    'jquery',
    'bootstrap',
    'jquery.stellar',
    'zurb/bower-foundation',
    'web-starter-kit',
)

BOWER_COMPONENTS_ROOT = '/home/msarhan/Src/codename_Small/Small/components'


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = '/home/msarhan/Src/codename_Small/Small/static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)


MEDIA_ROOT = '/home/msarhan/Src/codename_Small/Small/media/'

MEDIA_URL = '/media/'



#from django.core.urlresolvers import reverse_lazy
#
#LOGIN_URL = reverse_lazy('login')
#LOGOUT_URL = reverse_lazy('logout')
#LOGIN_REDIRECT_URL = reverse_lazy('Profile')
