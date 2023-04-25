from django.urls import path, include
from .views import (UserRegister, VerifyAccount, ChangePasswordApi, LoginApi, LogoutApi, RequestResetPasswordEmail,
                    PasswordCheckTokenApi, SetNewPasswordApi)

from rest_framework.routers import DefaultRouter


router= DefaultRouter()
router.register('users', UserRegister, basename='users')

urlpatterns = [ 
               
    path('', include(router.urls)),    
    path('activateaccount/', VerifyAccount.as_view(), name='email-verify'),
    path('login/', LoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),    
    
    #changing password not working on confirming passwd field      
    path('changepassword/', ChangePasswordApi.as_view(), name='changepassword'),
    path('request-reset-email/', RequestResetPasswordEmail.as_view(), name='request-reset-email'),
    path('resetpassword/<uidb64>/<token>/', PasswordCheckTokenApi.as_view(), name='password-reset-confirm'),
    path('resetpasswordcomplete/', SetNewPasswordApi.as_view(), name='password-reset-done'),
    
    
]