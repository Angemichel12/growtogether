from rest_framework.views import APIView
from .serializers import WriteAppointmentSerializer, ReadAppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from appointments.models import Appointment
from django.http import Http404

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

    
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = ReadAppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = WriteAppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appointment= self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)