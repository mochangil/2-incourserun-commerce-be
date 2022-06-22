from re import U
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from app.product.models import Product
from app.product.serializers import ProductListCreateSerializer, ProductListUpdateDeleteSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    # pagination_class = ProductPagination
    serializer_class = ProductListCreateSerializer

class ProductUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListUpdateDeleteSerializer
