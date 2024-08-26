import os
from celery.schedules import crontab
from kombu import Queue, Exchange


broker_url = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
result_backend = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

task_queues = (
    Queue('chats', Exchange('tasks'), routing_key='chats.#'),
)

task_default_queue = 'chats'
task_default_exchange_type = 'direct'

timezone = 'Europe/Moscow'