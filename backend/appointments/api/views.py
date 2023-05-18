from rest_framework.views import APIView
from .serializers import WriteAppointmentSerializer, ReadAppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from appointments.models import Appointment
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPatient
from drf_yasg.utils import swagger_auto_schema
from appointments.tasks import send_email_func


class UserAppointmentAPIView(APIView):

    @swagger_auto_schema(

        tags=['user action'],
        operation_summary='User_appointments',
        operation_description='User get all assigned appointments'

    )
    def get(self, request, format=None):
        appointments = Appointment.objects.all()
        serializer = ReadAppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=WriteAppointmentSerializer,
        tags=['user action'],
        operation_summary='User_Create_appointments',
        operation_description='User create appointments'

    )
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

    @swagger_auto_schema(

        tags=['user action'],
        operation_summary='appointment_detail',
        operation_description='User detail of appointment'

    )
    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = ReadAppointmentSerializer(appointment)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=WriteAppointmentSerializer,
        tags=['user action'],
        operation_summary='User_update_appointment',
        operation_description='User update appointment'

    )
    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = WriteAppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(

        tags=['user action'],
        operation_summary='User_delete_appointments',
        operation_description='User  delete assigned appointments'

    )
    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def test(request):
    send_email_func.delay()
    return Response("Message: Done")
