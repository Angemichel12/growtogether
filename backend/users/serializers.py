from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
	def create(self, clean_data):
		user_obj = User.objects.create_user(email=clean_data['email'], password=clean_data['password'],username = clean_data['username'],
					   first_name = clean_data['first_name'],last_name = clean_data['last_name'],birthdate = clean_data['birthdate'], phone = clean_data['phone'], is_email_verified = clean_data['is_email_verified'])
		user_obj.save()
		return user_obj

class ChangePasswordSerializer(serializers.Serializer):
    class Meta:
        extra_kwargs= {'confirm_newpassword': {'write_only': True,} }
                
    model= User
    
    old_password= serializers.CharField(required= True)
    new_password= serializers.CharField(required= True)
    confirm_newpassword= serializers.CharField(required= True, write_only=True)
    
    
