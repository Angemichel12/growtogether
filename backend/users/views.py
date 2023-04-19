from .serializers import UserRegisterSerializer, ReadOnlyUserSerializer
from rest_framework.views import APIView
from shortcuts.auto_generate import auto_username_password_generator
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class ReadUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ReadOnlyUserSerializer
class UserRegistrationAPIView(APIView):
    def post(self, request, format=None):
        cleaned_data = auto_username_password_generator(request.data)
        cleaned_data['password'] = make_password(cleaned_data['password'])
        serializer = UserRegisterSerializer(data=cleaned_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)