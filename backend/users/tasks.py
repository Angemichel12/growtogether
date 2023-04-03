from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_register_email(clean_data):
    fromEmail = settings.EMAIL_HOST_USER
    subject = f'Account is Successfull Created!'
    content = f'Dear {clean_data["first_name"]} your username is:{clean_data["username"]} and password: {clean_data["password"]}'
    user = clean_data["email"].strip()
    
    send_mail(
        subject,
        content,
        fromEmail,
        [user],
        fail_silently=False,
)
