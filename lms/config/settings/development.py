from .base import *

env = Env()
env.read_env(path=BASE_DIR / '.env-dev', override=True)

SECRET_KEY = env.str("SECRET_KEY", 'django-insecure-test-key')

DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", ['127.0.0.1',])


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MIDDLEWARE += "debug_toolbar.middleware.DebugToolbarMiddleware",


DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 10MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024 

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.alerts.AlertsPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]



if not os.path.exists('logs'):
    os.makedirs('logs')
# =============================================================================
# DEVELOPMENT LOGGING CONFIGURATION
# =============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {name} {module} {funcName}:{lineno} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '[{levelname}] {name} - {message}',
            'style': '{',
        },
        'colored': {
            'format': '\033[1;32m[{levelname}]\033[0m {asctime} \033[1;34m{name}\033[0m - {message}',
            'style': '{',
            'datefmt': '%H:%M:%S',
        },
        'django_server': {
            'format': '[{server_time}] {message}',
            'style': '{',
        },
    },
    
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
            'filters': ['require_debug_true'],
        },
        'django_server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django_server',
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
    
    'loggers': {
        'django': {
            'handlers': ['console', 'file_debug'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['django_server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Ваши приложения
        'account': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'account.views': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'account.models': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'account.tasks': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        
        'main': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'main.views': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'main.models': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'main.tasks': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        
        'structure': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'structure.views': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'structure.models': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'structure.tasks': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        
        'celery': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'requests': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'urllib3': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}