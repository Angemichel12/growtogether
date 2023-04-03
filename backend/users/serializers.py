from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'],username = clean_data['username'],
					   first_name = clean_data['first_name'],last_name = clean_data['last_name'],birthdate = clean_data['birthdate'])
		user_obj.save()
		return user_obj