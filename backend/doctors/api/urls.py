from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.DoctorsAPIView.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
]
