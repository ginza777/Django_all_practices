from django.urls import path
from .views import Home,WordList

urlpatterns = [
    path('',Home,name='home'),
    path('wordlist/',WordList.as_view(),name='wordlist')
]
