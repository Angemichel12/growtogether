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
    
class Checkup(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chekups")
    title = models.CharField(max_length=250)
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    checkup_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.user.username
    
class Vaccination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vaccinations")
    name = models.CharField(max_length=250)
    date_to = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.user.username
