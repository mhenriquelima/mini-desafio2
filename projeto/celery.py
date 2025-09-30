import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
app = Celery('projeto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'heartbeat-every-minute': {
        'task': 'app.tasks.heartbeat',
        'schedule': 60.0,  # every 60 seconds
    },
}