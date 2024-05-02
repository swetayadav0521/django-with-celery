from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_with_celery import settings


from celery import shared_task


@shared_task(bind=True)
def send_email(self):
    #users = get_user_model().objects.all()
    #for user in users:
    mail_subject = "Test via Celery and Django"
    message = "Kya haal hn"
    to_email = "swetayadav051@gmail.com"
    send_mail(subject=mail_subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[to_email], fail_silently=False )
    return "Done"

@shared_task(bind=True)
def show_value(self):
    for x in range(10):
        print(x)
    return "Done"