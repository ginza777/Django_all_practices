from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rest_framework import serializers
from .models import YourModel

class YourModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = YourModel
        fields = '__all__'
class CkeditorSerializer(serializers.ModelSerializer):

    class Meta:
        model = YourModel
        fields = '__all__'
