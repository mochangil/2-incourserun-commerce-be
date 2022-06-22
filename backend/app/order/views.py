from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from app.order.models import Order
from app.order.serializers import OrderListCreateSerializer, OrderListUpdateDeleteSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    # pagination_class = ProductPagination
    serializer_class = OrderListCreateSerializer

class OrderUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListUpdateDeleteSerializer
