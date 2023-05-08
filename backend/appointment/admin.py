from django.contrib import admin
from .models import SemesterAppointment, Vaccination


admin.site.register(SemesterAppointment)
admin.site.register(Vaccination)