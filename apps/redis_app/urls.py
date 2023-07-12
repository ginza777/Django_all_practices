from django.urls import path
from .views import RedisView

urlpatterns = [
    path('', RedisView.as_view(), name='redis'),
    ]