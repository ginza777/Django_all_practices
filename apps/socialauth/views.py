from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
User=get_user_model()


def login_page(request):
    return render(request, 'socialauth/login.html', {})
def register_page(request):
    return render(request, 'socialauth/register.html', {})



from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter,AppleOAuth2Client,AppleProvider
from dj_rest_auth.registration.views import SocialLoginView as AppleLoginView
class AppleLogin(AppleLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = 'http://127.0.0.1:2003'
    client_class = AppleOAuth2Client
