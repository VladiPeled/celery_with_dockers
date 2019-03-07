from __future__ import absolute_import
from celery import Celery

from config import CELERY_HOST, CELERY_PORT, CELERY_USER, CELERY_PASSWORD

app = Celery('test_celery',
             broker=f'amqp://{CELERY_USER}:{CELERY_PASSWORD}@{CELERY_HOST}:{CELERY_PORT}',
             backend='rpc://')

