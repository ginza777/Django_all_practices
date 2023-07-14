from random import randint
from django.contrib.sessions.backends.cache import SessionStore
from django.shortcuts import render
from twilio.rest import Client
from rest_framework import serializers, status
from apps.authentication.models import CustomUser as User
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return render(request, 'random_sms_verification.html')


def send_sms(phone, session_id):
    code = randint(1000, 9999)
    print(f"{phone} is sending {code}  session id {session_id}")
    session = SessionStore(session_key=session_id)
    session['sms_code'] = code
    session.save()


class LoginSerializers(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    sms_code = serializers.CharField(max_length=150, required=False)
    session_id = serializers.CharField(max_length=250, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        sms = attrs.get('sms_code')
        session_id = self.context.get('session_id')
        if phone and password and sms and session_id:
            user = User.objects.filter(phone=phone).first()
            if user:
                if user.check_password(password):
                    session_id = self.context.get('session_id')
                    session = SessionStore(session_key=session_id)
                    if str(session.get('sms_code')) == sms:
                        return user
                    else:
                        raise serializers.ValidationError('SMS code is not correct')
                else:
                    raise serializers.ValidationError('Password is not correct')
            else:
                raise serializers.ValidationError('User not found')
        elif phone and password:
            user = User.objects.filter(phone=phone).first()
            if user:
                if user.check_password(password):
                    return user
                else:
                    raise serializers.ValidationError('Password is not correct')
            else:
                raise serializers.ValidationError('User not found')
        else:
            raise serializers.ValidationError('Phone and password are required')


class LoginUser(APIView):
    serializers_class = LoginSerializers
    def get_queryset(self):
        return User.objects.all()
    def post(self, request):

        print(request.COOKIES.get('sessionid'))
        if self.request.COOKIES.get('sessionid') is None:
            print('session is none')
            serializer = LoginSerializers(data=self.request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            session = SessionStore()
            session.set_expiry(180)
            session.create()
            session_id = session.session_key
            send_sms(user.phone, session_id)
            response = Response(status=status.HTTP_202_ACCEPTED)
            # Set the session ID as a cookie in the response
            response.set_cookie('sessionid', session_id)
            return response
        else:
            print('session is not none')
            serializer = LoginSerializers(data=self.request.data, context={'session_id': request.COOKIES.get('sessionid')})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            session_id = request.COOKIES.get('sessionid')
            session = SessionStore(session_key=session_id)
            session.delete()
            response = Response(status=status.HTTP_201_CREATED)
            return response
