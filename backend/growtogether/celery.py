import os

from celery import Celery
from django.utils import timezone
from celery.schedules import crontab
import requests
from django.conf import settings
from django.urls import reverse



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'growtogether.settings')

app = Celery('growtogether')
app.conf.timezone = timezone.get_current_timezone_name()

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_vaccination_reminders': {
        'task': 'appointment.views.send_vaccinatio_reminder_view',
        'schedule': crontab(hour=8, minute=17), # send at 9am each day
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def ping(url):
    requests.get(url)