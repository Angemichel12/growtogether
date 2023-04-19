from django.urls import path
from .views import UserRegistrationAPIView,ReadUserList


urlpatterns = [
    path('', ReadUserList.as_view(), name='Users'),
    path('register/',UserRegistrationAPIView.as_view(), name='register'),
]
