from django.db import models


class Receptionist(models.Model):
    phone = models.CharField(max_length=13,)
