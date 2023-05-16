from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'PD'
        ACCEPTED = 'Accepted', 'AC'
    appointment_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return f'{self.user.username} {self.appointment_date}'
    

