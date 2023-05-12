from django.urls import path
from .views import ProductListView, ReviewListView

urlpatterns = [

    path('products/', ProductListView.as_view()),
    path('rewiews/', ReviewListView.as_view()),

]
