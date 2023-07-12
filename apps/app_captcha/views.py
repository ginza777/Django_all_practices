from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from apps.app_captcha.forms import LoginForm
from django.contrib import messages


def home(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("name")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:8000/en/swagger/")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "index.html", {"form": form})
