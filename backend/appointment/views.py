from django.shortcuts import render
from .serializers import ReadOnlyAppointmentSerializer, ReadOnlyCheckupSerializer, ReadOnlyVaccinationSerializer
from rest_framework import generics, permissions
from .models import SemesterAppointment, Checkup,Vaccination
from .tasks import vaccination_remender_email_task
from django.http import JsonResponse

class UserListAppointment(generics.ListAPIView):
    serializer_class = ReadOnlyAppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return SemesterAppointment.objects.filter(user=self.request.user)


class UserListCheckup(generics.ListAPIView):
    serializer_class = ReadOnlyCheckupSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return Checkup.objects.filter(user=self.request.user)
    
class UserListVaccination(generics.ListAPIView):
    serializer_class = ReadOnlyVaccinationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return Vaccination.objects.filter(user=self.request.user)
    
def send_vaccinatio_reminder_view(request):
    vaccination_remender_email_task.delay()
    return JsonResponse({'status': 'success'})