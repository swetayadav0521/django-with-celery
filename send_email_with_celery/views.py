import json
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email, show_value

from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.


def home(request):
    return HttpResponse("Django with Celery Application!!!")

def send_email_to_users(request):
    send_email.delay()
    return HttpResponse("Email has been sent successfully")

def check_worker(request):
    show_value.delay()
    return HttpResponse("Print")

def schedule_email(request):
    schedule, created  = CrontabSchedule.objects.get_or_create(hour= 1, minute= 10)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"1", task='send_email_with_celery.tasks.send_email') # ,args= json.dumps((2,3,)))
    return HttpResponse("Done")
    
