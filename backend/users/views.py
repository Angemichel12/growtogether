from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import  generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from django.urls import reverse
import jwt


# Create your views here.

class RegisterUserAPI(generics.GenericAPIView):
    serializer_class= RegisterSerializer
    
    def post(self, request):
        user= request.data
        serializer= self.serializer_class(data= user)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        user_data= serializer.data
        user= User.objects.get( email=user_data['email']) 
    
        token= RefreshToken.for_user(user).access_token 
        current_site= get_current_site(request).domain 
        rela_link= reverse('email-verify')        
        abs_url= 'http://'+current_site +rela_link+'?token='+str(token)
        
        email_body= 'Hello '+ user.username+'.\nPlease Use the link provided below to Verify Your GrowTogether Account.\n'+ abs_url
        data= {'email_body': email_body, 'to_email': user.email,
            'email_subject': 'Verify your GrowTogether Account.'}
        Util.send_email(data)     
                
        return Response(user_data, status= status.HTTP_201_CREATED)
    
class ActivateAccount(generics.GenericAPIView):
    def get(self, request):
        token= request.GET.get('token')