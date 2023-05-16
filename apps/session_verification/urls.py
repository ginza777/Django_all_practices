from django.urls import path
from .views import UserList,Home

urlpatterns=[
    path('',Home,name='userlist'),
    path('users/',UserList.as_view(),name='userlist'),
]
