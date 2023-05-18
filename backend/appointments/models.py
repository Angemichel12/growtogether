from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'PENDING'
        ACCEPTED = 'Accepted', 'ACCEPTED'
    appointment_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    def __str__(self):
        return f' {self.appointment_date}'
    

