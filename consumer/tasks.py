from __future__ import absolute_import
from consumer.celery import app


@app.task(name='task_name')
def whatever(**kwargs):
    print('CONSUMER - Im in whatever')
    print(f'CONSUMER -The data is {kwargs}')
    print('CONSUMER -OK')