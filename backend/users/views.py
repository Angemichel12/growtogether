from .serializers import (UserRegisterSerializer, 
                          ChangePasswordSerializer, 
                          ReadUserSerializer
)
from django.contrib.auth import get_user_model, authenticate
from .utils import Util
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import jwt
from datetime import date
from rest_framework.response import Response
from rest_framework import permissions, status, generics, viewsets
from rest_framework.views import APIView
from auto_tasks.auto_generate import auto_username_password_generator

from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema


User= get_user_model()

# Create your views here.


class UserRegister(viewsets.ViewSet):
    permission_classes = []
    @swagger_auto_schema(
        tags=['user action'],
        operation_description='List of all user in system',

    )
    def list(self, request):
        all_users= User.objects.filter(user_type='W')
        serializer= ReadUserSerializer(all_users, many= True) 
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        tags=['user action'],
        operation_description='This help to register Women',

    )
  
    def post(self, request):
        if User.is_doctor:
                        
            clean_data = auto_username_password_generator(request.data)
            serializer = UserRegisterSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                # user = serializer.create(clean_data)
                user = serializer.save()
                # Token.objects.get_or_create(user)[1]
                
                if user:
                    token= RefreshToken.for_user(user).access_token 
                    current_site= get_current_site(request).domain 
                    rela_link= reverse('email-verify')        
                    abs_url= 'http://'+current_site +rela_link+'?token='+str(token)
                    email_body= 'Hello '+ user.first_name+'.\n\nYour Account has been Created Successfully!\n\nUse the link provided below to activate your account.\n'+ abs_url
                    data= {
                        'email_body': email_body,
                        'to_email': user.email,
                        'email_subject': 'Activate Your Account on Growtogether system.'}
                    Util.send_email(data)
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response({'Error':'You are not Staff user'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class VerifyAccount(generics.GenericAPIView):
    def get(self, request):
        token= request.GET.get('token') 
        
        try:
            payload= jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user= User.objects.get(id=payload['user_id'])
            encryptedpassword=request.GET.get('password')
            
            if not user.is_active:
                user.is_active= True                             
                user.save()
                
                current_site= get_current_site(request).domain 
                rela_link= reverse('login')        
                abs_url= 'http://'+current_site +rela_link
                
                email_body= 'Hello '+ user.first_name+'.\n\nYour Account is successfully activated!\n\n Use Credentials provided below to login into your account.\n\n'+'Username: '+user.username+'\nPassword: '+ user.first_name+'@'+str(date.today().year) +'\n\nLogin Link:\n'+ abs_url
                data= {
                    'email_body': email_body,
                    'to_email': user.email,
                    'email_subject': 'Login into your Growtogether account.'}
                Util.send_email(data)
                # send_sms(request, user.phone)                
            return Response({'Email is Verified': 'Your Account is successfully activated!'}, status= status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError as identifier:
            return Response({'It\'s an Error':'Activation link expired!'}, status= status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'It\'s an Error':'Invalid token!'}, status= status.HTTP_400_BAD_REQUEST)
    

class LoginApi(APIView):
    permission_classes= [AllowAny, ]

    permission_classes = []
    @swagger_auto_schema(
        tags=['user action'],
        operation_description='user Login in system',

    )
            
    def post(self, request):
        username= request.data.get('username')
        passwd= request.data.get('password')
        user= authenticate(username= username, password= passwd)
        
        if user:
            if user.is_active:
                if user.user_type == "W":
                    token, created= Token.objects.get_or_create(user= user)
                    response= {
                    'Message':'Logged in successfully',
                    'Token': token.key
                }
                    return Response(data= response)
                return Response(data= {'Message':'You are not allowed to Login as Woman'},status= status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(data= {'Message':'Account is not allowed'}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data= {'Message':'Invalid credentials'},status= status.HTTP_401_UNAUTHORIZED)
    permission_classes = []

    @swagger_auto_schema(
        tags=['user action'],

    )   
    def get(self, request):
        content= {'user': str(request.user), 'auth':str(request.auth)}
        return Response(data= content, status= status.HTTP_200_OK)
    
class LogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes= [TokenAuthentication]

    permission_classes = []
    @swagger_auto_schema(
        tags=['user action'],

    )
    
    def get(self, request):
        content= {'user': str(request.user), 'auth':str(request.auth)}
        return Response(data= content, status= status.HTTP_200_OK)
    

    @swagger_auto_schema(
        tags=['user action'],

    )
        
    def post(self, request, format=None):
        request.auth.delete()
        return Response(data= {'Message':'User Logged out'})
    
        
class ChangePasswordApi(generics.UpdateAPIView):
    model= User
    serializer_class= ChangePasswordSerializer
    permission_classes= [IsAuthenticated, ]    
        
    def get_object(self, queryset= None):
        obj= self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object= self.get_object()
        serializer= self.get_serializer(data= request.data)
        
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Old Password is Wrong!'] }, status= status.HTTP_400_BAD_REQUEST)           
           
            if self.object.check_password(serializer.data.get('newpassword')):
                return Response({'Confirm_password': ['Failed to confirm new password!'] }, status= status.HTTP_400_BAD_REQUEST)           
            
            self.object.set_password(serializer.data.get('new_password'))   
            self.object.save() 
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

         
        
class ResetPasswordApi(APIView):
    pass


