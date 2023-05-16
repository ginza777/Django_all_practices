from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

User = get_user_model()


def Home(request):

    return render(request=request,template_name= 'userlist.html')
# Create your views here.

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class UserList(APIView):


    def get(self,request):
        user = User.objects.all().order_by('id')
        serializer=UserListSerializers(user,many=True)
        return Response(serializer.data)

