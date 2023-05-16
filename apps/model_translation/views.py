from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from apps.model_translation.models import Words


# Create your views here.

def Home(request):
    trans=_('hello')
    output=_("Welcome to my app")
    print(output)
    list=[]
    data={}
    words=Words.objects.all()
    for word in words:
        data['word']=word.word
        data['definition']=word.definition
        list.append(data)



    return render(request=request,template_name= 'modeltranslation.html',context={'home_data':list})

class RosettaListSerializers(serializers.ModelSerializer):


    class Meta:
        model = Words
        fields ='__all__'

class WordList(APIView ):
    serializer_class = RosettaListSerializers
    queryset = Words.objects.all().order_by('id')

    def get(self,request):
        wordlist=Words.objects.all()
        serializer=self.serializer_class(wordlist,many=True)
        return Response(serializer.data)



