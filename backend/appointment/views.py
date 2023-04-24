from rest_framework import viewsets
from .models import SemesterAppointment, Semesters
from .serializers import SemesterAppointmentSerializerModel, ReadOnlySemesterSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwner


class ReadOnlyListSemester(generics.ListAPIView):
    queryset = Semesters.objects.all()
    serializer_class = ReadOnlySemesterSerializer
    permission_classes = [permissions.IsAuthenticated]
class SemesterAppointmentListAPIView(generics.ListAPIView):
    serializer_class = SemesterAppointmentSerializerModel
    def get_queryset(self):
        user = self.request.user
        return SemesterAppointment.objects.filter(women=user)
    
    
