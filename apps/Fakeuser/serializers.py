from rest_framework import serializers
from .models import Fakeuser

class FakeuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakeuser
        fields = [
            'id',
            'name',
        ]
