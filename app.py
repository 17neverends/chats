from celery import Celery
from shared.bases.logger import Logger

celery_app = Celery(
    'chats',
    include=['tasks']
)

celery_app.config_from_object('config')
celery_app.autodiscover_tasks()

logger = Logger('chats', celery_app=celery_app)