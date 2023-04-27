from django.urls import path
from .views import UserListAppointment, UserListCheckup

urlpatterns = [
 path('', UserListAppointment.as_view(), name='appointment'),
 path('checkup/', UserListCheckup.as_view(), name='checkup'),
]