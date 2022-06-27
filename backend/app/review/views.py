from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from app.review.models import Reply, Review
from app.review.serializers import ReplyListCreateSerializer, ReplyUpdateDeleteSerializer, ReviewListCreateSerializer, ReviewListUpdateDeleteSerializer
from app.review.paginations import ReviewPagination


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListCreateSerializer
    pagination_class = ReviewPagination

class ReviewUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListUpdateDeleteSerializer

class ReplyListCreateView(ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplyListCreateSerializer

class ReplyUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplyUpdateDeleteSerializer
    