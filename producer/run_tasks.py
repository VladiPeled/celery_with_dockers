from producer.celery import app


if __name__ == '__main__':
    data = {'my_key': 'my_value'}
    print(f'Sending {data}')
    app.send_task('task_name',kwargs=data, queue='queue_name')
    print('Done')


