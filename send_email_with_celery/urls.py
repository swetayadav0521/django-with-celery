from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('send_email/', views.send_email_to_users, name='send_email'),
    path('check_worker/', views.check_worker, name='check_worker'),
    path('schedule_email/', views.schedule_email, name='schedule_email'),
]
