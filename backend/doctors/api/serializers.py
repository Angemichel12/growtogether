from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password','phone','birth_date')
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already in use.")
        return email
        
    def create(self, clean_data):
        doctor = User.objects.create(email=clean_data['email'],
                                      username = clean_data['username'], 
                                      first_name = clean_data['first_name'],
                                      last_name = clean_data['last_name'],
				      				is_active = False,
                                      is_staff = True,
                                      user_type = 'D'
				      )
        doctor.set_password(clean_data['password'])
        doctor.save()
        return doctor
        
