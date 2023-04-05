from .serializers import UserRegisterSerializer, ChangePasswordSerializer
from django.contrib.auth import get_user_model, authenticate
from .utils import Util
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import jwt

from rest_framework.response import Response
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from auto_tasks.auto_generate import auto_username_password_generator

UserModel= get_user_model()

# Create your views here.

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny, IsAuthenticated)
    def post(self, request):
        clean_data = auto_username_password_generator(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                token= RefreshToken.for_user(user).access_token 
                current_site= get_current_site(request).domain 
                rela_link= reverse('email-verify')        
                abs_url= 'http://'+current_site +rela_link+'?token='+str(token)
                email_body= 'Hello '+ user.first_name+'.\n\nYour Account has been Created Successfully!\n\nUse the link provided below to Verify your account.\n'+ abs_url
                data= {
                    'email_body': email_body,
                    'to_email': user.email,
                    'email_subject': 'Activate Your Account on Growtogether system.'}
                Util.send_email(data)                                                    
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                            
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class VerifyAccount(generics.GenericAPIView):
    def get(self, request):
        token= request.GET.get('token')
        try:
            payload= jwt.decode(token, settings.SECRET_KEY)
            user= UserModel.objects.get(id=payload['user_id'])
            if not user.is_email_verified:
                user.is_email_verified= True
                user.save()
            return Response({'email': 'Account is successfully activated!'}, status= status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError as identifier:
            return Response({'Its an Error':'Activation link expired!'}, status= status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'Its an Error':'Invalid token!'}, status= status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPI(generics.UpdateAPIView):
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
           
            if not serializer.data.get('confirm_newpassword')==serializer.data.get('new_password'):
                return Response({'Confirm_password': ['Failed to confirm new password!'] }, status= status.HTTP_400_BAD_REQUEST)           
            
            self.object.set_password(serializer.data.get('new_password'))   
            self.object.save() 
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)