from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','phone', 'password')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','phone','password')
