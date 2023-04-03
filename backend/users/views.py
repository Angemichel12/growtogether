from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework.views import APIView
from shortcuts.auto_generate import auto_username_password_generator
class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = auto_username_password_generator(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
