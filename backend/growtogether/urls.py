from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Growtogether API",
      default_version='1.0.0',
      description="Grow together API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    #path('swagger/schema', schema_view.with_ui('swagger', cache_timeout=0),name="swagger_schema"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  
    path('api/', include('users.urls')),
    path('api/auth/', obtain_auth_token),

    # Doctors app
    path('api/doctor/', include('doctors.api.urls')),

    # Appointments app
    path('api/appointments/', include('appointments.api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



    
