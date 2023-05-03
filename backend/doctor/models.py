from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create Doctor model

class doctor(models.Model):
    Obstetrician = 'OB'
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'

    department_choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Obstetrician,'Obstetrician'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ]

    qualification_choices =[
         ('PHD','PHD'),
         ('Doctor','Dr'),
         ('Masters','Ms'),
        ('A0','A0'),
        ('A1','A1'),
        ('A2','A2')
    ]
    department = models.CharField(max_length=3, choices=department_choices, default=Obstetrician)
    phone = models.CharField(max_length=10)
    qualification = models.CharField(max_length=10, choices=qualification_choices, default='A2')
    birth_date = models.DateField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        return self.user.first_name +" "+self.user.last_name
    @property
    def get_user_id(self):
        return self.user.id
    @property 
    def get_phone(self):
        return self.phone
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)