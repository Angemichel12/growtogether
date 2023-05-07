from django.db import models
from django.contrib.auth.models import AbstractUser



USER_CHOICES = [
    ('D', 'Doctor'),
    ('W', 'Woman'),
    ('R', 'Receptionist'),
    ('HR', 'HR'),
    ('C', 'Consultator')
]
class User(AbstractUser):
    user_type = models.CharField(max_length=3, choices=USER_CHOICES, default='W')
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

