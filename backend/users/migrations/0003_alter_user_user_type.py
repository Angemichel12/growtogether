# Generated by Django 4.2 on 2023-05-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_birth_date_delete_woman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Doctor'), ('W', 'Woman'), ('R', 'Receptionist'), ('HR', 'HR'), ('C', 'Consultator')], default='W', max_length=3),
        ),
    ]
