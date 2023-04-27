from django.shortcuts import render
from .serializers import ReadOnlyAppointmentSerializer, ReadOnlyCheckupSerializer
from rest_framework import generics, permissions
from .models import SemesterAppointment, Checkup

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
