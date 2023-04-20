from django.urls import path
from rest_framework import routers
from .views import SemesterAppointment, ReadOnlyListSemester
router = routers.SimpleRouter()


router.register(r'semester_appointment', SemesterAppointment, basename='semester_appointment')

urlpatterns = [
    path('semester/', ReadOnlyListSemester.as_view(), name='semester'),
]+router.urls