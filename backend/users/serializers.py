from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.encoding import force_str, smart_str, smart_text, DjangoUnicodeDecodeError   
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

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
    
# class RequestPasswordResetSerializer(serializers.Serializer):
#     email= serializers.EmailField(min_length=2)
#     class Meta:
#         fields= ['email'] 
#     def validate(self, attrs):
#         try:
#             email= attrs.get('email', '')
#             if UserModel.objects.filter(email= email).exists():
#                 user= UserModel.objects.get(email= email)
#                 uidb64= 
                
#                 return attrs
#         except Exception as e:
#             pass
#         return super().validate(attrs)
        
