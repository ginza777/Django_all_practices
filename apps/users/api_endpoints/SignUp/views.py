from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer


class RegisterView(TokenObtainPairView, CreateAPIView):

    @swagger_auto_schema(
        request_body=RegisterSerializer,)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=serializer.data
            print(user)
            username = serializer.validated_data.get("username")


            tokenserializer = TokenObtainPairSerializer(
                data={"username": username, "password": serializer.validated_data.get("password")}
            )
            tokenserializer.is_valid(raise_exception=True)

            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token.refresh_token)
            user_logged_in.send(sender=user.__class__, request=request, user=user)

            return Response(status=status.HTTP_201_CREATED, data={"message": "User created successfully",
                                                                  "user": user,
                                                                  "access_token": access_token,
                                                                  "refresh_token": refresh_token,
                                                                  })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
