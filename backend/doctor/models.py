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
    department = models.CharField(max_length=3, choices=department_choices, default=Obstetrician)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        return self.user.first_name +" "+self.user.last_name
    @property
    def get_user_id(self):
        return self.user.id
    @property 
    def get_phone(self):
        return self.user.phone
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)