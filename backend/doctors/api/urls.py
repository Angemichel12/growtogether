from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.DoctorsAPIView.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
    path('logout/', views.User_logout),
    path('doctor_activation/', views.VerifyAccount.as_view(), name='doctor-verify')
]
