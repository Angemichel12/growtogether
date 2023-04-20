from django.urls import path
from .views import UserRegister, VerifyAccount, ChangePasswordAPI

urlpatterns = [ 
               
    path('', UserRegister.as_view(), name='registeruser'),
    path('registeruser/', UserRegister.as_view(), name='registeruser'),
    path('activate-account/', VerifyAccount.as_view(), name='email-verify'),
        
    path('change-password/', ChangePasswordAPI.as_view(), name='changepassword'),
    
    
]

