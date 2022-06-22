from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from app.review.models import Review
from app.review.serializers import ReviewListCreateSerializer, ReviewListUpdateDeleteSerializer


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    # pagination_class = ProductPagination
    serializer_class = ReviewListCreateSerializer

class ReviewUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListUpdateDeleteSerializer
