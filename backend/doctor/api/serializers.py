from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from doctor.models import doctor

User = get_user_model()


class DoctorRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username:",validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(label="Email:",validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(label="First_name:")
    last_name = serializers.CharField(label="Last_name:")
    password = serializers.CharField(label="Password:", style={'input_type':'password'}, write_only=True, min_length=8,help_text="Your password must contain at least 8 character and should not be entirely numeric.")
    password2=serializers.CharField(label='Confirm password:',style={'input_type': 'password'},  write_only=True)


    def validate_password(self, password):
        if password.isdigit() or len(password) < 8:
            raise serializers.ValidationError('Password should contain letters and more 8 characters')
        return password
    
    def validate(self, data):
        password=data.get('password')
        password2=data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        return data
    
    def create(self, validated_data):
        user= User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
        user.set_password(validated_data['password'])
        user.save()
        group_doctor, created = Group.objects.get_or_create(name='doctor')
        group_doctor.user_set.add(user)
        return user
    
class DoctorProfileSerializer(serializers.Serializer):
    Obstetrician = 'OB'
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'

    department=serializers.ChoiceField(label='Department:', choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Obstetrician,'Obstetrician'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ])
    phone = serializers.CharField(label="Phone", min_length=10)
    birth_date = serializers.DateField(label="Birth_date")
    qualification= serializers.ChoiceField(label='Qualification', choices=[ ('PHD','PHD'),
        ('Doctor','Dr'),
        ('Masters','Ms'),
        ('A0','A0'),
        ('A1','A1'),
        ('A2','A2')])
    
    def validate_phone(self, phone):
        if phone.isdigit()==False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return phone


    
    def create(self, validated_data):
        new_doctor= doctor.objects.create(
            department=validated_data['department'],
            qualification=validated_data['qualification'],
            phone=validated_data['phone'],
            birth_date=validated_data['birth_date'],
            user=validated_data['user']
        )
        return new_doctor
    
    def update(self, instance, validated_data):
        instance.department=validated_data.get('department', instance.department)
        instance.qualification=validated_data.get('qualification', instance.qualification)
        instance.phone=validated_data.get('phone', instance.phone)
        instance.birth_date=validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance
