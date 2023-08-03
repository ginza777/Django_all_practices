from django.urls import path

from .views import *
from . import api_endpoints
app_name = "users"

urlpatterns = [
    path("signup/", api_endpoints.RegisterView.as_view(), name="register"),

    ]
