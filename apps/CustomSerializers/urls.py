from django.urls import path
from .views import *

urlpatterns = [
    path("", CustomSerializersView.as_view(), name="user-list"),
    path("choice/", CustomChoiceView.as_view(), name="user-list"),
    path("filter/", FakeUserFilter.as_view(), name="user-list"),
]
