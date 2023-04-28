from django.contrib import admin
from .models import SemesterAppointment, Checkup, Vaccination


admin.site.register(SemesterAppointment)
admin.site.register(Checkup)
admin.site.register(Vaccination)