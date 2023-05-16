from rest_framework.views import APIView
from .serializers import WriteAppointmentSerializer
from rest_framework.response import Response
from rest_framework import status


class UserAppointmentAPIView(APIView):
    def post(self, request, format=None):
        serializer = WriteAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)