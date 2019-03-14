FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD config.py /app/config.py
ADD ssl_cert/ca_certificate.pem /var/ssl/ca_certificate.pem
ADD ssl_cert/client_certificate.pem /var/ssl/client_certificate.pem
ADD ssl_cert/client_key.pem /var/ssl/client_key.pem
ADD ./producer/ /app/producer/
WORKDIR /app/
RUN pip install -r requirements.txt && rm /app/requirements.txt
ENTRYPOINT python -m producer.run_tasks
