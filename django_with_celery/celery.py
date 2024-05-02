from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django_with_celery import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_celery.settings')

app = Celery('django_with_celery')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_email_with_celery.tasks.send_email',
        'schedule': crontab(hour=20, minute=13),
        #'args': '',
    }
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")