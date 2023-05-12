from rest_framework import serializers
from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    # name=serializers.CharField(source='username.username')

    class Meta:
        model = Review
        fields = [
            'text',
            'stars',
            'username',
        ]
