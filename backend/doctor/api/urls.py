from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='api_doctor_registration'),
]

