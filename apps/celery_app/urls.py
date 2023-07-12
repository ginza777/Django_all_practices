from django.urls import path
from .views import YourModelListAPIView

urlpatterns = [
    path('', YourModelListAPIView.as_view(), name='your-models'),
]
