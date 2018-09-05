from lbworkflow.tests.settings import *  # NOQA

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'testproject',
    'stronghold',
    'impersonate',
    'debug_toolbar'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRONGHOLD_PUBLIC_URLS = [
    r'^/admin/',
]

MIDDLEWARE += [
    'impersonate.middleware.ImpersonateMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'testproject.urls'

LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'
IMPERSONATE_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL_ = '/media/'
MEDIA_URL = MEDIA_URL_

LBWF_APPS.update({
    'issue': 'lbworkflow.tests.issue',
})

TEMPLATE_DEBUG = True
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = '127.0.0.1'