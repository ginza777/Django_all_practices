from django.urls import path
from .views import *

urlpatterns = [
    path('', Vacancies.as_view()),
]
