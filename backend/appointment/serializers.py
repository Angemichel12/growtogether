from rest_framework import serializers
from .models import SemesterAppointment, Semesters

class ReadOnlySemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'

class SemesterAppointmentSerializerModel(serializers.ModelSerializer):
    semester = serializers.SlugRelatedField(slug_field='title', queryset=Semesters.objects.all())
    class Meta:
        model = SemesterAppointment
        fields = ('semester','test_date','utelas_height','child_situation', 'child_heart_rate','appointment','description')
