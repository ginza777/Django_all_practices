from django import forms
from captcha.fields import ReCaptchaField
from apps.app_captcha.models import CaptchaUser


class LoginForm(forms.Form):
    secret_word = forms.CharField(max_length=100)
    captcha = ReCaptchaField()

    class Meta:
        model = CaptchaUser
        fields = ["name", "password", "captcha", "secret_word"]
