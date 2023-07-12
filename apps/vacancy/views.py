from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from . import serializers
from . import models


# Create your views here.


class Vacancies(APIView):
    throttle_classes = [UserRateThrottle]

    queryset = models.Vacancies.objects.all()
    serializer_class = serializers.VacanciesListSerializers

    def get_queryset(self):
        return models.Vacancies.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = serializers.VacanciesListSerializers(self.queryset, many=False)
        return Response(serializer.data)
