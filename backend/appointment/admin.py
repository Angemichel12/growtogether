from django.contrib import admin
from .models import SemesterAppointment, Vaccination, Appointment


admin.site.register(SemesterAppointment)
admin.site.register(Vaccination)
admin.site.register(Appointment)