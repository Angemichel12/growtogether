from django.urls import path, include
from .views import (UserRegister, VerifyAccount,
                     ChangePasswordApi, 
                     LoginApi, LogoutApi,
                     ResetPasswordApi,
                    WomanProfileView,
                     CreateWomenProfileView )

from rest_framework.routers import DefaultRouter



router= DefaultRouter()
router.register('users', UserRegister, basename='users')

urlpatterns = [ 
            
    path('', include(router.urls)),    
    path('activateaccount/', VerifyAccount.as_view(), name='email-verify'),
    path('login/', LoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),
    path('profile/', WomanProfileView.as_view(), name='api_woman_profile'), 
    path('create_profile/',CreateWomenProfileView.as_view(), name='create_profile'),

    
    #changing password not working on confirming passwd field      
    path('changepassword/', ChangePasswordApi.as_view(), name='changepassword'),
    path('resetpassword/', ResetPasswordApi.as_view(), name='resetpassword'), 
    
    
]