from rest_framework import viewsets
from .models import SemesterAppointment, Semesters
from .serializers import SemesterAppointmentSerializerModel, ReadOnlySemesterSerializer
from rest_framework import generics


class ReadOnlyListSemester(generics.ListAPIView):
    queryset = Semesters.objects.all()
    serializer_class = ReadOnlySemesterSerializer
class SemesterAppointment(viewsets.ModelViewSet):
    queryset = SemesterAppointment.objects.all()
    serializer_class = SemesterAppointmentSerializerModel
