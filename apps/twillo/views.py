from random import randint
from django.contrib.sessions.backends.cache import SessionStore
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, LoginSerializerSms
import datetime


class LoginView(APIView):
    def post(self, request):
        print('view', request.data)
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        session_id = send_sms(user)
        # Return a response
        response = Response({'message': 'sms ni kiriting'}, status=status.HTTP_202_ACCEPTED)
        # Set the session ID as a cookie in the response
        response.set_cookie('sessionid', session_id)
        print(response)
        return response


class LoginViewSms(APIView):
    def post(self, request, *args, **kwargs):
        print('sms: ', self.request.data)
        serializer = LoginSerializerSms(data=request.data, context={'session_id': self.request.COOKIES.get('sessionid')})
        serializer.is_valid(raise_exception=True)

        return Response({'message': 'sms ni kiriting'}, status=status.HTTP_200_OK)


def send_sms(user: object):
    phone = ''
    session = SessionStore()
    session.set_expiry(1800)
    session.create()
    session_id = session.session_key
    code = randint(1000, 9999)
    session['sms_code'] = code
    # file
    with open('./base.txt', 'a+') as file:
        text = f'{phone}  {code} {session_id}  {datetime.datetime.now().time().strftime("%H:%M:%S")}'
        print(text)
        file.write(text + '\n')
    return session_id
