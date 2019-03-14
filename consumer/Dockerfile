FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD config.py /app/config.py
ADD ssl_cert/ca_certificate.pem /var/ssl/ca_certificate.pem
ADD ssl_cert/client_certificate.pem /var/ssl/client_certificate.pem
ADD ssl_cert/client_key.pem /var/ssl/client_key.pem
ADD ./consumer/ /app/consumer/
WORKDIR /app/
RUN pip install -r requirements.txt && rm /app/requirements.txt
ENTRYPOINT celery -A consumer worker --loglevel=info -Q queue_name

