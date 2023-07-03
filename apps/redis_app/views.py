from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework import serializers, status
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

class RedisSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=200)



class RedisView(APIView):
    throttle_classes = [UserRateThrottle]


    def post(self, request):
        serializer = RedisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['word']
        reversed_text = text[::-1]
        response_data = {
            'original_text': text,
            'reversed_text': reversed_text
        }
        r.set(text, reversed_text)
        print(r.get(text)  )

        return Response(response_data, status=status.HTTP_200_OK)
