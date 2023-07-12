from django.urls import path
from .views import *
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login_twillo'),
    path('', home, name='home_twillo')
]
