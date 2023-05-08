from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class HospitalAdmin(models.Model):
    phone = models.CharField(max_length=13)
    birt_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admins")
