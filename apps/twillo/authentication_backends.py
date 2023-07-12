# authentication_backends.py
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()

class PhonePasswordAuthBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        user = User.objects.filter(phone=phone).first()

        if user and user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
