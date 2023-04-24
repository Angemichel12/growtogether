from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


USER_CHOICES = [
    ('D', 'Doctor'),
    ('W', 'Woman'),
    ('R', 'Receptionist'),
    ('HR', 'HR'),
    ('C', 'Consultator')
]
class User(AbstractUser):
    user_type = models.CharField(max_length=3, choices=USER_CHOICES, default='W')
    birthdate = models.DateField(null= True)
    is_email_verified = models.BooleanField(default=False)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)
    phone = PhoneNumberField(null= True) 
    is_email_verified = models.BooleanField(default=False, blank=True)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)
            
    def is_doctor(self):
        if self.user_type == 'D':
            return True
        else:
            return False

    def is_woman(self):
        if self.user_type == 'W':
            return True
        else:
            return False

    def is_receptionist(self):
        if self.user_type == 'R':
            return True
        else:
            return False
    def is_consultator(self):
        if self.user_type == 'C':
            return True
        else:
            return False

    def is_HR(self):
        if self.user_type == 'HR':
            return True
        else:
            return False
        
    def __str__(self):
        return self.username
    
class Woman(models.Model):
    woman = models.ForeignKey(User, on_delete=models.CASCADE, related_name="women")
    pregnant_time = models.IntegerField()
    beget_time = models.IntegerField()
    beget_date = models.DateField()
    province = models.CharField(max_length=20)
    district = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    cell = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    hospital = models.CharField(max_length=100)
    Health_center = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.woman.username


