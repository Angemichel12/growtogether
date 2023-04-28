from celery import shared_task
import datetime
from .models import Vaccination
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def vaccination_remender_email_task(result):
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    vaccinations = Vaccination.objects.filter(date_to=NextDay_Date)
    if vaccinations:
        subject = 'Reminder: Meeting tomorrow'
        message = 'You have a meeting tomorrow. Here are the details:\n\n'
        for vaccination in vaccinations:
            message += f'Dear {vaccination.user.first_name}\n We write This email to remaind you to come at hospital to get vaccine of {vaccination.name}\n On {vaccination.date_to}\n because \n{vaccination.description}\n'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [vaccination.user.email],fail_silently=True,)