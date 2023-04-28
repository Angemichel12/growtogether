from django.urls import path
from .views import *

urlpatterns = [
 path('', UserListAppointment.as_view(), name='appointment'),
 path('checkup/', UserListCheckup.as_view(), name='checkup'),
 path('vaccination/', UserListVaccination.as_view(), name='vaccinatio'),
 path('remender_vaccination/', send_vaccinatio_reminder_view, name="remender"),
]