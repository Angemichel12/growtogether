from django.urls import path, include
from .views import (UserRegister, VerifyAccount,
                     ChangePasswordApi, 
                     LoginApi, LogoutApi,
                     ResetPasswordApi,
                    WomanProfileView,
                     CreateWomenProfileView,
                      WomanAppointmentViewset,
                       SemesterAppointmentAPIView,
                        VaccinationAPIView )

from rest_framework.routers import DefaultRouter



router= DefaultRouter()
router.register('users', UserRegister, basename='users')
router.register('appointment', WomanAppointmentViewset, basename='appointment')

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


    # Semester Appointment urls
    path('semester/', SemesterAppointmentAPIView.as_view()),

    # Vaccination urls
    path('vaccination/', VaccinationAPIView.as_view())
    
]