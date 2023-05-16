from django.urls import path
from .views import *

urlpatterns=[
    path('',Home,name='wordlist'),
    path('words/',WordList.as_view(),name='wordlist'),
]
