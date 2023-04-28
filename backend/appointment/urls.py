from django.urls import path
from .views import UserListAppointment

urlpatterns = [
 path('', UserListAppointment.as_view(), name='appointment'),
]