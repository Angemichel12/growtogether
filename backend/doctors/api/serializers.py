from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class RegisterDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        

        def create(self, validated_data):
            user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
            user.set_password(validated_data['password'])
            user.is_staff = True
            user.save()
            group_doctor, created = Group.objects.get_or_create(name='doctor')
            group_doctor.user_set.add(user)
            return user
