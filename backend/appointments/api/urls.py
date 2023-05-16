from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserAppointmentAPIView.as_view(), name='user_appointmens'),
]
