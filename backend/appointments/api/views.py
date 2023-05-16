from rest_framework.views import APIView
from .serializers import WriteAppointmentSerializer, ReadAppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from appointments.models import Appointment


class UserAppointmentAPIView(APIView):

    def get(self, request, format=None):
        appointments = Appointment.objects.filter(user=request.user)
        serializer = ReadAppointmentSerializer(appointments, many=True)
        return Response(serializer.data)



    def post(self, request, format=None):
        serializer = WriteAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)