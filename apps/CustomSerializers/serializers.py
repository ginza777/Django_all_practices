from rest_framework import serializers

from apps.Fakeuser.models import Fakeuser,default_gender


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakeuser
        fields = '__all__'

class CustomChoiceField(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    number=serializers.ChoiceField(choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
