from django.urls import path
from .views import RegisterUserAPI, ActivateAccount

urlpatterns = [      
    path('registeruser/', RegisterUserAPI.as_view(), name='registeruser'),
    path('account-activation/', ActivateAccount.as_view(), name='email-verify'),
    
    
]