from django.template.loader import render_to_string
from django.shortcuts import redirect
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework.views import APIView
from shortcuts.auto_generate import auto_username_password_generator
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model

def activate(request, uidb64, token):
	User = get_user_model()
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except:
		user=None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		print('Successful activated!')
	else:
		print("Not successful activated")


def activateEmail(request, user):
    current_site = get_current_site(request)
    mail_subject = "Activate your user account."
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(str(user.pk).encode('utf-8')),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    to_email=user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        print("message send successfull")
    else:
        print("Not successfull")

		
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = auto_username_password_generator(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            user.is_active = False
            user.save()
            activateEmail(request, user)  # pass user object as argument
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

