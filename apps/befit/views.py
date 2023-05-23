
from rest_framework.generics import ListCreateAPIView
from .serializers import ProductSerializers, ReviewSerializers
from .models import Product, Review


class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class ReviewListView(ListCreateAPIView):
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
