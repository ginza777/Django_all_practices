from rest_framework import serializers
from . import models
from django.db.models import Count


class VacanciesListSerializers(serializers.Serializer):
    vacancies_count = serializers.SerializerMethodField()
    resumes_count = serializers.SerializerMethodField()
    count_of_company = serializers.SerializerMethodField()

    def get_vacancies_count(self, obj):
        vacancies_count = models.Vacancies.objects.count()
        vacancies_count = int(vacancies_count)
        return vacancies_count

    def get_resumes_count(self, obj):
        resumes_count = models.Resume.objects.count()
        return resumes_count

    def get_count_of_company(self, obj):
        counts = models.Company.objects.annotate(vacancies_count=Count('vacancies')).filter(
            vacancies_count__gt=0).count()
        return counts
