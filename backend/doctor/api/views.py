from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorRegistrationSerializer,DoctorProfileSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from doctor.models import doctor
from .permissions import IsDoctor
from rest_framework.permissions import AllowAny


# API endpoint for Doctor Login
class CustomAuthToken(ObtainAuthToken):

    """This class returns custom Authentication token only for Doctor"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        account_approval = user.groups.filter(name='doctor').exists()
        if user.user_type != 'D':
            return Response(
                {
                    'message': "Your account is not approved by admin yet!"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        elif account_approval==False:
            return Response(
                {
                    'message': "You are not authorised to login as a doctor"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        else:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'Message':'You are login successful',
                'token': token.key
            },status=status.HTTP_200_OK)

# API endpoint for Doctor Registration
class RegistrationView(APIView):
    permission_classes=[AllowAny,]
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

class doctorProfileView(APIView):
    """"API endpoint for doctor profile view/update-- Only accessble by doctors"""

    permission_classes=[IsDoctor]

    def get(self, request, format=None):
        user = request.user
        profile = doctor.objects.filter(user=user).get()
        userSerializer=DoctorRegistrationSerializer(user)
        profileSerializer = DoctorProfileSerializer(profile)
        return Response({
            'user_data':userSerializer.data,
            'profile_data':profileSerializer.data

        }, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        user = request.user
        profile = doctor.objects.filter(user=user).get()
        profileSerializer = DoctorProfileSerializer(
            instance=profile, data=request.data.get('profile_data'), partial=True)
        if profileSerializer.is_valid():
            profileSerializer.save()
            return Response({
                'profile_data':profileSerializer.data
            }, status=status.HTTP_200_OK)
        return Response({
                'profile_data':profileSerializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    

# API endpoint for doctor profile view/update-- only accessble by doctors

class DoctorProfileView(APIView):
    permission_classes=[IsDoctor]
    
    def get(self, request, format=None):
        user = request.user
        profile = doctor.objects.filter(user=user).get()
        userSerializer = DoctorRegistrationSerializer(user)
        profileSerializer=DoctorProfileSerializer(profile)

        return Response({
            'user_data':userSerializer.data,
            'profile_data':profileSerializer.data
        }, status=status.HTTP_200_OK)
    
    def put(self, request, format=None):
        user = request.user
        profile = doctor.objects.filter(user=user).get()
        profileSerializer = DoctorProfileSerializer(instance=profile, data=request.data.get('profile_data'), partial=True)
        if profileSerializer.is_valid():
            profileSerializer.save()
            return Response({
                'profile_data':profileSerializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'profile_data':profileSerializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
