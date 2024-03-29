"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True

SITE_ID = 1

SOCKETIO_HOST = 'socketio.example.com'
SOCKETIO_PORT = 80
DASHBOARD_REQUIRE_LOGIN = False
DASHBOARD_MESSENGER_URL = 'http://example.com/'

PROJECT_ROOT = os.path.dirname(__file__)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'md_playerpointer_users.tests.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(__file__, '../../../static/')
MEDIA_ROOT = os.path.join(__file__, '../../../media/')
STATICFILES_DIRS = (
    os.path.join(__file__, 'test_static'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'test_app', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'django_socketio',
]

INTERNAL_APPS = [
    'metrics_dashboard',
    'md_playerpointer_users',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
