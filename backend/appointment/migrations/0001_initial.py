# Generated by Django 4.2 on 2023-05-08 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_to', models.DateField()),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Sem1', 'Semester1'), ('Sem2', 'Semester2'), ('Sem3', 'Semester3')], default='Sem1', max_length=4)),
                ('test_date', models.DateField()),
                ('utelas_height', models.CharField(max_length=250)),
                ('children_situation', models.CharField(max_length=250)),
                ('appointment_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)),
                ('department', models.CharField(choices=[('CL', 'Cardiologist'), ('DL', 'Dermatologists'), ('OB', 'Obstetrician'), ('EMC', 'Emergency Medicine Specialists'), ('IL', 'Immunologists'), ('AL', 'Anesthesiologists'), ('CRS', 'Colon and Rectal Surgeons')], max_length=20)),
                ('woman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
