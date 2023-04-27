from .serializers import (UserRegisterSerializer, ChangePasswordSerializer, RequestResetPasswordSerializer,
                          SetNewPasswordSerializer)
from django.contrib.auth import get_user_model, authenticate
from .utils import Util
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import jwt

from rest_framework.response import Response
from rest_framework import permissions, status, generics, viewsets
from rest_framework.views import APIView
from auto_tasks.auto_generate import auto_username_password_generator
from .models import User

from rest_framework.authtoken.models import Token
from django.utils.encoding import smart_str, force_bytes,force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator


UserModel= get_user_model()

# Create your views here.


class UserRegister(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny, IsAuthenticated]
    
    def list(self, request):
        all_users= User.objects.all()
        serializer= UserRegisterSerializer(all_users, many= True) 
        return Response(serializer.data)
        
    def post(self, request):
        if User.is_receptionist or User.is_HR:
                        
            clean_data = auto_username_password_generator(request.data)
            serializer = UserRegisterSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                # user = serializer.create(clean_data)
                user = serializer.save()
                # Token.objects.get_or_create(user)
                
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
            if not user.is_email_verified:
                user.is_email_verified= True                             
                user.save()
                
                current_site= get_current_site(request).domain 
                rela_link= reverse('login')        
                abs_url= 'http://'+current_site +rela_link
                
                email_body= 'Hello '+ user.first_name+'.\n\nYour Account is successfully activated!\n\n Use Credentials provided below to login into your account.\n\n'+'Username: '+user.username+'\nPassword: '+ request.user.password+ '\n\nLogin Link:\n'+ abs_url
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
            
    def post(self, request):
        username= request.data.get('username')
        passwd= request.data.get('password')
        user= authenticate(username= username, password= passwd)
        
        if user:
            if user.is_active:
                token, created= Token.objects.get_or_create(user= user)
                response= {
                    'Message':'Logged in successfully',
                    'Token': token.key
                }
                return Response(data= response)
            else:
                return Response(data= {'Message':'Account is not allowed'}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data= {'Message':'Invalid credentials'},status= status.HTTP_401_UNAUTHORIZED)
         
    def get(self, request):
        content= {'user': str(request.user), 'auth':str(request.auth)}
        return Response(data= content, status= status.HTTP_200_OK)
    
class LogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes= [TokenAuthentication]
    
    def get(self, request):
        content= {'user': str(request.user), 'auth':str(request.auth)}
        return Response(data= content, status= status.HTTP_200_OK)
        
    def post(self, request, format=None):
        request.auth.delete()
        return Response(data= {'Message':'User Logged out'})
    
        
class ChangePasswordApi(generics.UpdateAPIView):
    model= UserModel
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
                return Response({'Confirm_pas sword': ['Failed to confirm new password!'] }, status= status.HTTP_400_BAD_REQUEST)           
            
            self.object.set_password(serializer.data.get('new_password'))   
            self.object.save() 
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
         
        
class RequestResetPasswordEmail(generics.GenericAPIView):
    serializer_class= RequestResetPasswordSerializer
    
    def post(self, request):
        serializer= self.serializer_class(data= request.data)        
        email= request.data['email']
        
        if UserModel.objects.filter(email=email).exists():
            user= User.objects.get(email=email)
            
            uidb64= urlsafe_base64_encode(force_bytes(user.pk) )
            token= PasswordResetTokenGenerator().make_token(user)
            
            current_site= get_current_site(request= request).domain 
            rela_link= reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token} )        
            abs_url= 'http://'+current_site + rela_link
            
            email_body= 'Hello '+ user.first_name+'.\n\nUse the link below to reset your password.\n'+ abs_url
            data= {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': 'Reset Your Password -- Growtogether System.'}
            Util.send_email(data)
            return Response({'Email sent': 'We sent you an email with reset password link.' })                
        return Response({'Error': 'Account with this email not found!' })
    
class PasswordCheckTokenApi(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            id= smart_str(urlsafe_base64_decode(uidb64))
            user= User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'Error': 'Token is invalid, Request new one.' })
            return Response({'Success': True, 'Message':'Credentials are valid', 'uidb64': uidb64, 'token': token })
 
        except DjangoUnicodeDecodeError as identifier:
                return Response({'Error': 'Token is invalid, Request new one.' })
           
class SetNewPasswordApi(generics.GenericAPIView):
    serializer_class= SetNewPasswordSerializer
    permission_classes= [AllowAny, ]
       
    def patch(self, request):
        serializer= self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception= True)        
        return Response({'Success': True, 'Message':'Password reset successfully'}, status= status.HTTP_200_OK)

                       
        