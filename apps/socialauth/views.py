from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
User=get_user_model()


def login_page(request):
    return render(request, 'socialauth/login.html', {})
def register_page(request):
    return render(request, 'socialauth/register.html', {})