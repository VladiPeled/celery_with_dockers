# celery_with_dockers
Running Producer, Consumer Dockers with Celery and RabbitMQ

## Specifications

There are 3 dockers:
1. Producer
2. Consumer
3. RabbitMQ

Producer sends kwargs with task name to RabbitMQ queue (From producer/run_tasks).
Consumer performs long pull to the queue. 
Once there is a message, the consumer worker runs the specific task which has the name that the producer sends. (consumer/tasks)

The producer doesn't know the code of the consumer.

## Building

docker-compose build

## Running

docker-compose up -d




