from django.shortcuts import render
from .serializers import RegisterDoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from auto_tasks.auto_generate import fullname_generator
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from users.utils import Util
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password

class CustomAuthToken(ObtainAuthToken):

    """This class returns custom Authentication token only for Doctor"""
    @swagger_auto_schema(
        
        tags=['doctor action'],
        operation_description='Login as Doctor'

    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_staff != True:
            return Response(
                {
                    'message': "Your account is not approved by admin yet!"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        elif user.user_type == False:
            return Response(
                {
                    'message': "You are not authorised to login as a doctor"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        else:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            },status=status.HTTP_200_OK)
        
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')
        


class DoctorsAPIView(APIView):

    @swagger_auto_schema(
        request_body=RegisterDoctorSerializer,
        tags=['doctor action'],

    )
    def post(self, request, format=None):
        clear_data = request.data
        clear_data=fullname_generator(clear_data)
        password = clear_data.get('password')
        confirm_password = clear_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

        clear_data['password']= make_password(clear_data['password'])
        serializer = RegisterDoctorSerializer(data=clear_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
                    token= RefreshToken.for_user(user).access_token 
                    current_site= get_current_site(request).domain 
                    rela_link= reverse('email-verify')        
                    abs_url= 'http://'+current_site +rela_link+'?token='+str(token)
                    email_body= 'Hello Dr. '+ user.first_name+'.\n\nYour Account has been Created Successfully!\n\nUse the link provided below to activate your account.\n'+ abs_url
                    data= {
                        'email_body': email_body,
                        'to_email': user.email,
                        'email_subject': 'Activate Your Account on Growtogether system.'}
                    Util.send_email(data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)