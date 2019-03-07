FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD config.py /app/config.py
ADD ./producer/ /app/producer/
WORKDIR /app/
RUN pip install -r requirements.txt && rm /app/requirements.txt
ENTRYPOINT python -m producer.run_tasks
