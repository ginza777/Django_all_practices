from django.shortcuts import render
from apps.app_captcha.forms import LoginForm
from apps.app_captcha.models import CaptchaUser


def home(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = CaptchaUser.objects.create(name=request.POST.get("name"), password=request.POST.get("password"))
            print(user)
            user.save()

    else:
        form = LoginForm()

    return render(request, "index.html", {"form": form})
