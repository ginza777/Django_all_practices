from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login_sms/', LoginViewSms.as_view(), name='login_Sms'),

    ]
