from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from apps.rosetta_example.models import Words


# Create your views here.

def home(request):
    trans = _('hello')

    return render(request=request, template_name='rosseta.html', context={'data': trans})


class RosettaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


class WordList(APIView):
    serializer_class = RosettaListSerializers
    queryset = Words.objects.all().order_by('id')

    def get(self, request):
        wordlist = Words.objects.all()
        serializer = self.serializer_class(wordlist, many=True)

        return Response(serializer.data)
