# Generated by Django 4.1.7 on 2023-04-26 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_email_verified_user_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='forget_password_token',
        ),
    ]
