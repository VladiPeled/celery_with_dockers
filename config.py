import os

CELERY_HOST = os.getenv('CELERY_HOST', 'rabbit-mq')
CELERY_PORT = os.getenv('CELERY_PORT', 5672)
CELERY_USER = os.getenv('CELERY_USER', 'rabbit')
CELERY_PASSWORD = os.getenv('CELERY_PASSWORD', 'rabbit')