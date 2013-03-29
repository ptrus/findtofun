# Django settings for findtofun project.
import re, os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'C:/Users/Nejc/Dropbox/findtofun/tftdb.db',  # Or path to database file if using sqlite3.
        'NAME': '/Users/TipyTop/Desktop/Dropbox/findtofun/baza.db',
        #'NAME': 'C:/???/findtofun/ftfdb.db',
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Ljubljana'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in events' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rlhx#ek24br(*m%1j(h*xtkolk*%tcj5)d15i(phqf7-@t4ny0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
#    'fb.middleware.SSLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'fb.middleware.ExampleSocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'findtofun.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'findtofun.wsgi.application'

PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = (
     os.path.join(PROJECT_DIR, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
#    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'app',
#    'south',
    'social_auth',
    'fb',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# report broken links - 404 error if referrer is in request
SEND_BROKEN_LINK_EMAILS = True
# the opposite. Ignore 404 urls.
IGNORABLE_404_URLS = (
    re.compile(r'\.(php|cgi)$'),
    re.compile(r'^/phpmyadmin/'),

    # The following example shows how to exclude some
    # conventional URLs that browsers and crawlers often request
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

#DEFAULT_EXCEPTION_REPORTER_FILTER = 'path.to.your.CustomExceptionReporterFilter'
USE_ETAGS = True

#===============================================================================
# Django Social Auth
#===============================================================================

AUTH_USER_MODEL = "fb.MyUser"

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_type_backends',
)

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.user.update_user_details',
    'fb.pipeline.write_extra_details',
)

FACEBOOK_APP_ID              = '436119486471234'
FACEBOOK_API_SECRET          = '02124a5e2b45255e1aa3bb9330e3fbe9'
FACEBOOK_EXTENDED_PERMISSIONS = [
     'create_event',
     'rsvp_event',
]

LOGIN_URL          = '/login'

LOGIN_REDIRECT_URL = '/done'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/done?type=social'
FACEBOOK_SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/done?type=social&backend=fb'

LOGIN_ERROR_URL    = '/error?type=login'
FACEBOOK_LOGIN_ERROR_URL = "/error?type=login&backend=fb"
SOCIAL_AUTH_BACKEND_ERROR_URL = '/error?type=backend'
FACEBOOK_SOCIAL_AUTH_BACKEND_ERROR_URL = "/error?type=backend&backend=fb"

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/done?type=newUser'
FACEBOOK_SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/done?type=newUser&backend=fb'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/disconnect'
FACEBOOK_SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/disconnect?backend=fb'

SOCIAL_AUTH_INACTIVE_USER_URL = '/social'
FACEBOOK_SOCIAL_AUTH_INACTIVE_USER_URL = '/social?type=inactive&backend=fb'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_URLOPEN_TIMEOUT = 30
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_SESSION_EXPIRATION = False
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
# SOCIAL_AUTH_CREATE_USERS = False

# facebook testing
TEST_FACEBOOK_USER = 'testing_account'
TEST_FACEBOOK_PASSWORD = 'password_for_testing_account'