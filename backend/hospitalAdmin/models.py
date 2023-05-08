from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HospitalAdmin(models.Model):
    birth_date = models.DateField()
    phone = models.CharField(max_length=13)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="hospital_admin")

    def __str__(self):
        return self.user.first_name
