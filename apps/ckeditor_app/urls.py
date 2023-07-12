from django.conf.urls import include
from django.urls import path
from .views import FileUploadAPIView,CkeditorList
urlpatterns = [

    path('uploader/', include('ckeditor_uploader.urls')),
    path('upload/', FileUploadAPIView.as_view(), name='file-upload'),
    path('',CkeditorList.as_view(),name='ckeditor')
]



