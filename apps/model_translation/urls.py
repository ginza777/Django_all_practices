from django.urls import path
from .views import home, WordList

urlpatterns = [
    path('', home, name='home'),
    path('wordlist/', WordList.as_view(), name='wordlist')
]
