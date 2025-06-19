from .base import *

env = Env()
env.read_env(path=BASE_DIR / '.env-production', override=True)

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS",)

ADMINS = [
    ('Islombek Orifov', 'islombekorifov0199@gmail.com'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USERNAME'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOSTNAME'),
        'PORT': env.int('DB_PORT', 5432),
    }
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 10MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024


# PRODUCTION LOGGING CONFIGURATION
# =============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {name} {module} {funcName}:{lineno} {process:d} {thread:d} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '[{levelname}] {asctime} {name} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'syslog': {
            'format': 'django[{process:d}]: [{levelname}] {name} - {message}',
            'style': '{',
        },
        'json': {
            'format': '{"level": "{levelname}", "time": "{asctime}", "logger": "{name}", "module": "{module}", "function": "{funcName}", "line": {lineno}, "message": "{message}"}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'skip_suspicious_operations': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: 'SuspiciousOperation' not in record.getMessage()
        },
    },
    
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.log',
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 10,
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/error.log',
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 10,
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/security.log',
            'maxBytes': 1024*1024*25,  # 25 MB
            'backupCount': 5,
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
        'file_requests': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/requests.log',
            'maxBytes': 1024*1024*100,  # 100 MB
            'backupCount': 15,
            'formatter': 'simple',
            'filters': ['require_debug_false', 'skip_suspicious_operations'],
        },
        'file_db': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/database.log',
            'maxBytes': 1024*1024*25,  # 25 MB
            'backupCount': 5,
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'formatter': 'syslog',
            'filters': ['require_debug_false'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
            'include_html': True,
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
        },
        'json_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.json',
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 10,
            'formatter': 'json',
            'filters': ['require_debug_false'],
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    
    'root': {
        'level': 'WARNING',
        'handlers': ['console', 'file_error', 'syslog'],
    },
    
    'loggers': {
        'django': {
            'handlers': ['file_info', 'file_error', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file_requests', 'file_error', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_requests'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_db'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security', 'mail_admins', 'syslog'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['file_security'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        
        'account': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'account.views': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'account.models': {
            'handlers': ['file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        'account.tasks': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'account.api': {
            'handlers': ['file_requests', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'account.auth': {
            'handlers': ['file_security', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        
        'main': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'main.views': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'main.models': {
            'handlers': ['file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        'main.tasks': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'main.api': {
            'handlers': ['file_requests', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'main.auth': {
            'handlers': ['file_security', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        
        'structure': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'structure.views': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'structure.models': {
            'handlers': ['file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        'structure.tasks': {
            'handlers': ['file_info', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'structure.api': {
            'handlers': ['file_requests', 'file_error', 'json_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'structure.auth': {
            'handlers': ['file_security', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        
        # Третьесторонние библиотеки
        'celery': {
            'handlers': ['file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery.task': {
            'handlers': ['file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        'gunicorn': {
            'handlers': ['file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False,
        },
        'gunicorn.access': {
            'handlers': ['file_requests'],
            'level': 'INFO',
            'propagate': False,
        },
        'gunicorn.error': {
            'handlers': ['file_error', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'requests': {
            'handlers': ['file_info'],
            'level': 'WARNING',
            'propagate': False,
        },
        'urllib3': {
            'handlers': ['null'],
            'propagate': False,
        },
        'boto3': {
            'handlers': ['file_info'],
            'level': 'WARNING',
            'propagate': False,
        },
        'botocore': {
            'handlers': ['file_info'],
            'level': 'WARNING',
            'propagate': False,
        },
        'redis': {
            'handlers': ['file_info', 'file_error'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
