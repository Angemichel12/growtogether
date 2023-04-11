from django.urls import path
from .views import UserRegister, activate

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('activate/<uidb64>/<token>', activate, name='activate'),
]
