from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from .models import Woman
from appointment.models import (Appointment, SemesterAppointment, Vaccination)



UserModel = get_user_model()
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ['username']


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ['email','password', 'first_name','last_name','username','is_active']

  
	def create(self, clean_data):
     
		user_obj = UserModel.objects.create(email=clean_data['email'],
                                      password= make_password(clean_data['password']),
                                      username = clean_data['username'], 
                                      first_name = clean_data['first_name'],
                                      last_name = clean_data['last_name'],
				      				is_active = False
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
    

class WomanProfileSerializer(serializers.Serializer):
	birth_date = serializers.DateField(label="Birth Date")
	phone = serializers.CharField(label='Phone', max_length=13)

	def validate_phone(self, phone):
		if phone.isdigit()==False:
			raise serializers.ValidationError('Please Enter a valid Phone number!')
		return phone
	
	def create(self, validated_data):
		
		new_woman = Woman.objects.create(birth_date=validated_data['birth_date'],
				   phone=validated_data['phone'])
		return new_woman
	
	def update(self, instance, validated_data):
		instance.birth_date=validated_data.get('phone', instance.birth_date)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.save()
		return instance
	


class WriteProfileSerializer(serializers.ModelSerializer):
    user =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Woman
        fields = ['birth_date', 'phone', 'user']
	
class ReadAppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = ('id','date', 'time', 'status', 'department')

class WriteAppointmentSerializer(serializers.ModelSerializer):
	woman = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = Appointment
		fields = ('date', 'time', 'status', 'department','woman')

class ReadSemesterAppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = SemesterAppointment
		fields = ('semester', 'test_date', 'utelas_height','children_situation','appointment_date','status','description')


class ReadVaccinationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vaccination
		fields = ('name','date_to','description')

		
		
        
