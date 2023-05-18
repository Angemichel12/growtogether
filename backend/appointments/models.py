from django.db import models


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'PENDING'
        ACCEPTED = 'Accepted', 'ACCEPTED'
    appointment_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    def __str__(self):
        return f' {self.appointment_date}'
    

