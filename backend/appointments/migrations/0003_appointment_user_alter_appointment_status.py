# Generated by Django 4.2 on 2023-05-18 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0002_remove_appointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Accepted', 'ACCEPTED')], default='Pending', max_length=10),
        ),
    ]