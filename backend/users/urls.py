from django.urls import path, include
from .views import (UserRegister, VerifyAccount, ChangePasswordAPI, LoginApi, )

from rest_framework.routers import DefaultRouter


router= DefaultRouter()
router.register('users', UserRegister, basename='users')

urlpatterns = [ 
               
    path('', include(router.urls)),    
    path('activateaccount/', VerifyAccount.as_view(), name='email-verify'),
    path('login/', LoginApi.as_view(), name='login'),
    # path('logout/', LogoutApi.as_view(), name='logout'),
    
    
    #change password not working on confirming passwd      
    path('changepassword/', ChangePasswordAPI.as_view(), name='changepassword')
    
    
]