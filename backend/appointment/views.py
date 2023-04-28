from django.shortcuts import render
from .serializers import ReadOnlyAppointmentSerializer
from rest_framework import generics, permissions
from .models import SemesterAppointment

class UserListAppointment(generics.ListAPIView):
    serializer_class = ReadOnlyAppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return SemesterAppointment.objects.filter(user=self.request.user)
