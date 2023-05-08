from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SemesterAppointment(models.Model):
    class ChoiceSemester(models.TextChoices):
        SEMESTER1= 'Sem1', 'Semester1'
        SEMESTER2= 'Sem2', 'Semester2'
        SEMESTER3= 'Sem3', 'Semester3'


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='semester_appointments')
    semester = models.CharField(max_length=4, choices=ChoiceSemester.choices, default=ChoiceSemester.SEMESTER1)
    test_date = models.DateField()
    utelas_height = models.CharField(max_length=250)
    children_situation = models.CharField(max_length=250)
    appointment_date = models.DateField()
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    Obstetrician = 'OB'
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'

    department_choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Obstetrician,'Obstetrician'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ]
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    woman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='woman')
    department = models.CharField(max_length=20, choices=department_choices)

    def __str__(self):
        return "Patient - {} Doc- {} At {} {}".format(self.patient, self.doctor, self.date, self.time)
    
class Vaccination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vaccinations")
    name = models.CharField(max_length=250)
    date_to = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.user.username
