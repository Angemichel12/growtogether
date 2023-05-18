import os
from celery.schedules import crontab

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'growtogether.settings')

app = Celery('growtogether')
app.conf.enable_utc = False
app.conf.update(timezone='Africa/Kigali')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Celery Beat Settings

app.conf.beat_schedule = {
    'send-mail-every-day-at-14': {
        'task': 'appointments.tasks.send_email_func',
        'schedule': crontab(hour=20, minute=00)
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
