from rest_framework import serializers
from appointments.models import Appointment


class WriteAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'reason')

class ReadAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'reason','status')
