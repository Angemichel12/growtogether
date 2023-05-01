from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorRegistrationSerializer,DoctorProfileSerializer

# API endpoint for Doctor Registration
class RegistrationView(APIView):
    permission_classes=[]
    def post(self,request,format=None):
        registrationSerializer = DoctorRegistrationSerializer(data=request.data.get('user_data'))
        profileSerializer = DoctorProfileSerializer(data=request.data.get('profile_data'))
        checkregistration = registrationSerializer.is_valid(raise_exception=True)
        checkprofile = profileSerializer.is_valid(raise_exception=True)
        if checkregistration and checkprofile:
            doctor = registrationSerializer.save()
            profileSerializer.save(user=doctor)
            return Response({
                "user_data":registrationSerializer.data,
                "profile_data":profileSerializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'user_data': registrationSerializer.errors,
                'profile_data': profileSerializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
