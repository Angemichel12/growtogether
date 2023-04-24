from django.urls import path
from .views import SemesterAppointmentListAPIView, ReadOnlyListSemester

urlpatterns = [
    path('semester/', ReadOnlyListSemester.as_view(), name='semester'),
    path('', SemesterAppointmentListAPIView.as_view())
]