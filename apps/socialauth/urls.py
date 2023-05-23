from django.urls import path
from . views import login_page, register_page

urlpatterns = [
    path('', login_page, name='login_url'),
    path('register/', register_page, name='register_url'),


    ]