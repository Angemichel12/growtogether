from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegister, VerifyAccount, ChangePasswordAPI

urlpatterns = [ 
    path('login/', obtain_auth_token, name='obtain-auth-token'),
    path('', UserRegister.as_view(), name='registeruser'),
    path('registeruser/', UserRegister.as_view(), name='registeruser'),
    path('activate-account/', VerifyAccount.as_view(), name='email-verify'),
        
    path('change-password/', ChangePasswordAPI.as_view(), name='changepassword'),
    
    
]

