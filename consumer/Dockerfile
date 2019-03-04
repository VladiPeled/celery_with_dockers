FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD ./consumer/ /app/consumer/
WORKDIR /app/
RUN pip install -r requirements.txt && rm /app/requirements.txt
ENTRYPOINT celery -A consumer worker --loglevel=info -Q queue_name

