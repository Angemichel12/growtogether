from rest_framework import serializers
from appointments.models import Appointment


class WriteAppointmentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'reason','user')

class ReadAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'reason','status')
