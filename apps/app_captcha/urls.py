from django.urls import path
from apps.app_captcha.views import home

urlpatterns = [
    path("", home, name="home")
]
