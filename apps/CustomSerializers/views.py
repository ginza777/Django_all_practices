import django_filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.Fakeuser.models import Fakeuser
from .serializers import CustomSerializer, CustomChoiceField


# Create your views here.


# pagination

class CustomPagination(PageNumberPagination):
    page_size = 3  # Number of items to include in each page
    page_size_query_param = 22  # Custom query parameter to specify page size
    max_page_size = 10  # Maximum page size allowed


class CustomSerializersView(ListAPIView):
    queryset = Fakeuser.objects.all()
    serializer_class = CustomSerializer
    pagination_class = CustomPagination


# choice api

class CustomChoiceView(APIView):
    serializer_class = CustomChoiceField

    def post(self, request, *args, **kwargs):
        print(request.data)

        return Response({"message": "Got some data!"})


# filter api

class FakeUserFilter(ListAPIView):
    queryset = Fakeuser.objects.all()
    serializer_class = CustomSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'gender', 'married']
