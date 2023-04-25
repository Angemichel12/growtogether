from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from rest_framework.authtoken.models import Token
from django.utils.encoding import smart_str, force_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator


UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
		extra_kwargs = {
			'is_email_verified': {'read_only': True}
		}  
  
	def create(self, clean_data):
     
		user_obj = UserModel.objects.create(email=clean_data['email'],
                                      password= make_password(clean_data['password']),
                                      username = clean_data['username'], 
                                      first_name = clean_data['first_name'],
                                      last_name = clean_data['last_name'],
                                      birthdate = clean_data['birthdate'],
                                      phone = clean_data['phone'])		  
		return user_obj


class ChangePasswordSerializer(serializers.Serializer):
    class Meta:
        extra_kwargs= {
            'confirm_newpassword': {'write_only': True,} 
		}                
    model= UserModel
    
    old_password= serializers.CharField(required= True)
    new_password= serializers.CharField(required= True)
    confirm_newpassword= serializers.CharField(required= True, write_only=True)
    
class RequestResetPasswordSerializer(serializers.Serializer):
    email= serializers.EmailField(min_length= 2)
    class Meta:
        fields= ['email']        
        
class SetNewPasswordSerializer(serializers.Serializer):
    newpassword= serializers.CharField(min_length=6, max_length= 64, required=True)
    uidb64= serializers.CharField(min_length= 1, write_only= True, required=True)
    token= serializers.CharField(min_length= 1, write_only= True, required=True)
    
    class Meta:
        fields= '__all__'
        
    def validate(self, request):
        try:
            newpassword= request.get('newpassword')
            uidb64= request.get('uidb64')
            token= request.get('token')
            
            id= force_str(urlsafe_base64_decode(uidb64))
            user= User.objects.get(id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response('Reset link invalid', 401)
            
            user.set_password(newpassword)
            user.save()
        except Exception as e:
            return Response('Reset link invalid', 401)
        return super().validate(request)
            
            
            
              
