from django.shortcuts import render
from .models import Fakeuser
from .serializers import FakeuserSerializer
# Create your views here.


from rest_framework import generics

class FakeUserList(generics.ListAPIView):
    queryset = Fakeuser.objects.filter(id__lte=10)
    serializer_class = FakeuserSerializer
