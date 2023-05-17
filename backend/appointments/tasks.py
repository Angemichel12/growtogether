from celery import shared_task
from appointments.models import Appointment
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta





@shared_task(bind=True)
def send_email_func(self):
    current_date = datetime.now()
    tomorrow = current_date + timedelta(days=1)
    tomorrow_date = tomorrow.date()
    appointments = Appointment.objects.filter(appointment_date=tomorrow_date)

    for appointment in appointments:
        mail_subject = "Hi Women"
        message = "We hope this email finds you well, We are reminder you have appointment tomorrow"
        to_email = appointment.user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,        
            
        )
    return 'Done'