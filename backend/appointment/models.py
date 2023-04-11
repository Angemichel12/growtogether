from django.db import models
from users.models import User

class Semesters(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class SemesterAppointment(models.Model):
    women = models.ForeignKey(User, on_delete=models.CASCADE, related_name='women_semesters')
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, related_name="semester_appointments")
    test_date = models.DateField()
    utelas_height = models.CharField(max_length=5)
    child_situation = models.CharField(max_length=250)
    child_heart_rate = models.CharField(max_length=250)
    appointment = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.semester.title
