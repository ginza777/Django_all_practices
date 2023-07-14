
from django.urls import path

from .views import FakeUserList

urlpatterns = [
    path('', FakeUserList.as_view(), name='fakeuser-list'),
]
