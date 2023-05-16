from django.urls import path, include
from .views import (UserRegister, VerifyAccount,
                     ChangePasswordApi, 
                     LoginApi, LogoutApi,
                     ResetPasswordApi,
                     UserRegister,)





urlpatterns = [ 
            
    path('users/',UserRegister.as_view(), name="user_register"),    
    path('activateaccount/', VerifyAccount.as_view(), name='email-verify'),
    path('login/', LoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),

    
    #changing password not working on confirming passwd field      
    path('changepassword/', ChangePasswordApi.as_view(), name='changepassword'),
    path('resetpassword/', ResetPasswordApi.as_view(), name='resetpassword'), 

]