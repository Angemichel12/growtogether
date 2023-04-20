from django.contrib.auth import get_user_model
from rest_framework import serializers
from appointment.serializers import SemesterAppointmentSerializerModel

User = get_user_model()

class ReadOnlyUserSerializer(serializers.ModelSerializer):
    semester = SemesterAppointmentSerializerModel(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','phone','password')
