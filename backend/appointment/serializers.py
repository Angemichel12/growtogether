from rest_framework import serializers
from .models import SemesterAppointment, Semesters
from django.contrib.auth import get_user_model

User = get_user_model()

class ReadOnlySemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'

class SemesterAppointmentSerializerModel(serializers.ModelSerializer):
    semester = serializers.SlugRelatedField(slug_field='title', queryset=Semesters.objects.all())
    women = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = SemesterAppointment
        fields = ('women','semester','test_date','utelas_height','child_situation', 'child_heart_rate','appointment','description')
