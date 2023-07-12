from django.shortcuts import render
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from apps.model_translation.models import Words
from rest_framework import generics


# Create your views here.

def home(request):
    output = _("Welcome to my app")
    print(output)
    list2 = []
    words = Words.objects.all()
    for word in words:
        data = {}
        data['word'] = word.word
        data['definition'] = word.definition
        list2.append(data)
    return render(request=request, template_name='modeltranslation.html', context={'home_data': list2})


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
