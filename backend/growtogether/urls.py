from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('appointment/', include('appointment.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='obtain_pair_view'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_view'),
    
]
