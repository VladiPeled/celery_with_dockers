from __future__ import absolute_import
from celery import Celery
import ssl

from config import CELERY_HOST, CELERY_PORT, CELERY_USER, CELERY_PASSWORD

app = Celery('test_celery',
             broker=f'amqp://{CELERY_USER}:{CELERY_PASSWORD}@{CELERY_HOST}:{CELERY_PORT}',
             backend='rpc://')

app.conf.update(
broker_use_ssl = {
    'keyfile': '/var/ssl/client_key.pem',
    'certfile': '/var/ssl/client_certificate.pem',
    'ca_certs': '/var/ssl/ca_certificate.pem',
    'cert_reqs': ssl.CERT_REQUIRED
}
)