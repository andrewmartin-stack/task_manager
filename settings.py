"""Django settings for task_manager project in production."""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Debugging disabled for production
DEBUG = False

# Allowed hosts configured for local and specific devices
ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.151', '192.168.1.64']

if DEBUG:
    DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'test_db.sqlite3')

# Database switched to SQLite for lightweight setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'prod_db.sqlite3'),
    }
}
