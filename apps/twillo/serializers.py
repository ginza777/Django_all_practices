# serializers.py
from django.contrib.auth import get_user_model
from django.contrib.sessions.backends.cache import SessionStore
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)


    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        if phone and password:
            user = User.objects.filter(phone=phone).first()

            if user:
                if user.check_password(password):
                    attrs['user'] = user
                    return attrs
                else:
                    raise serializers.ValidationError('Invalid password')
            else:
                raise serializers.ValidationError('User not found')
        else:
            raise serializers.ValidationError('Phone and password are required')


class LoginSerializerSms(serializers.Serializer):
    phone = serializers.CharField(max_length=150)
    sms = serializers.CharField(max_length=150)

    def validate(self, attrs):
        phone = attrs.get('phone')
        sms = attrs.get('sms')
        session_id = self.context.get('session_id')

        if phone and sms and session_id:
            user = User.objects.filter(phone=phone).first()
            if user:
                session = SessionStore(session_key=session_id)
                if str(session.get('sms')) == sms:
                    session.delete()
                    attrs['user'] = user
                    return attrs
                else:
                    raise serializers.ValidationError('SMS code is not correct')
            else:
                raise serializers.ValidationError('User not found')
        else:
            raise serializers.ValidationError('sms is invalid')
