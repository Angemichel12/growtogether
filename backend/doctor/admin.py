from django.contrib import admin
from . models import doctor

class doctorAdmin(admin.ModelAdmin):
    list_display=['get_full_name','department', 'get_phone', 'user']

admin.site.register(doctor,doctorAdmin)
