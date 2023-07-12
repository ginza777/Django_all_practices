from rest_framework.views import APIView
from rest_framework.response import Response
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelListAPIView(APIView):
    def get(self, request):
        your_models = YourModel.objects.all()
        serializer = YourModelSerializer(your_models, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
