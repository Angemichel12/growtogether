from django.shortcuts import render
from .serializers import RegisterDoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from auto_tasks.auto_generate import fullname_generator


class CustomAuthToken(ObtainAuthToken):

    """This class returns custom Authentication token only for Doctor"""
    @swagger_auto_schema(
        
        tags=['doctor action'],
        operation_description='Login as Doctor'

    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_staff != True:
            return Response(
                {
                    'message': "Your account is not approved by admin yet!"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        elif user.user_type == False:
            return Response(
                {
                    'message': "You are not authorised to login as a doctor"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        else:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            },status=status.HTTP_200_OK)


class DoctorsAPIView(APIView):

    @swagger_auto_schema(
        request_body=RegisterDoctorSerializer,
        tags=['doctor action'],

    )
    def post(self, request, format=None):
        clear_data = request.data
        clear_data=fullname_generator(clear_data)
        serializer = RegisterDoctorSerializer(data=clear_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)