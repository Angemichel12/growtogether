from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password




UserModel = get_user_model()
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ['username']


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ['email','password', 'first_name','last_name','username','is_active','user_type']

	def validate_email(self, email):
		if UserModel.objects.filter(email=email).exists():
			raise serializers.ValidationError("This email is already in use.")
		return email

  
	def create(self, clean_data):
     
		user_obj = UserModel.objects.create(email=clean_data['email'],
                                      password= make_password(clean_data['password']),
                                      username = clean_data['username'], 
                                      first_name = clean_data['first_name'],
                                      last_name = clean_data['last_name'],
				      				is_active = False,
								      user_type= 'W'
				      )
		return user_obj
class ReadUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields =['email', 'first_name','last_name']
		


class ChangePasswordSerializer(serializers.Serializer):
    class Meta:
        extra_kwargs= {
            'confirm_newpassword': {'write_only': True,} 
		}                
    model= UserModel
    
    old_password= serializers.CharField(required= True)
    new_password= serializers.CharField(required= True)
    confirm_newpassword= serializers.CharField(required= True, write_only=True)
    

