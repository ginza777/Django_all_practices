from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import YourModel
from .serializers import YourModelSerializer,CkeditorSerializer

class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.FILES['upload']
        # Faylni o'zgartirish, saqlash yoki boshqa kerakli amallarni bajarish
        # Fayl URL sini qaytarish
        file_url = 'http://example.com/uploads/' + file_obj.name  # Fayl URL sini o'zgartiring
        return Response({'url': file_url})



class CkeditorList(ListCreateAPIView):
    serializer_class = CkeditorSerializer
    def get_queryset(self):
        return YourModel.objects.all()
