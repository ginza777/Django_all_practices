from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from apps.model_translation.models import Words
from django.utils.translation import activate
from modeltranslation.utils import get_language
from rest_framework import generics


# Create your views here.

def Home(request):
    trans = _('hello')
    output = _("Welcome to my app")
    print(output)
    list = []

    words = Words.objects.all()
    for word in words:
        data = {}
        data['word'] = word.word
        data['definition'] = word.definition
        list.append(data)
    return render(request=request, template_name='modeltranslation.html', context={'home_data': list})


class RosettaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = [
            'word',
            'definition'
        ]


class WordList(generics.ListAPIView):
    serializer_class = RosettaListSerializers
    queryset = Words.objects.all().order_by('id')
    pagination_class = None
