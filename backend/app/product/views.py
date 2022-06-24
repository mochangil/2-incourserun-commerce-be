from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from django.db.models.functions import Coalesce
from app.product.models import Product,Hashtag
from app.product.serializers import HashtagSerializer, ProductListCreateSerializer, ProductListUpdateDeleteSerializer
from app.review.models import Review
from django.db.models import Subquery, OuterRef,Avg, Count


class ProductListCreateView(ListCreateAPIView):
    avg_rating_subquery = Review.objects.filter(product=OuterRef('id')).values('product').annotate(avg=Avg('rating')).values('avg')
    review_count_subquery = Review.objects.filter(product=OuterRef('id')).values('product').annotate(cnt=Count('id')).values('cnt')

    queryset = Product.objects.annotate(
        avg_rating = Coalesce(Subquery(avg_rating_subquery), 0.0),
        review_count = Coalesce(Subquery(review_count_subquery), 0)
    )
    # rating_queries = Review.objects.filter(product=OuterRef('productname')).annotate(avg=Avg('rating')).annotate(cnt=Count('rating'))
    # # cnt_rating_queries = Review.objects.filter(product=OuterRef('productname')).annotate(cnt=Count('rating'))
    # queryset = Product.objects.annotate(avg_rating=Subquery(rating_queries.values('avg')[:1]))
    # queryset = queryset.annotate(cnt_rating=Subquery(rating_queries.values('cnt')[:1]))
    # pagination_class = ProductPagination
    serializer_class = ProductListCreateSerializer

class ProductUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    avg_rating_subquery = Review.objects.filter(product=OuterRef('id')).values('product').annotate(avg=Avg('rating')).values('avg')
    review_count_subquery = Review.objects.filter(product=OuterRef('id')).values('product').annotate(cnt=Count('id')).values('cnt')

    queryset = Product.objects.annotate(
        avg_rating = Coalesce(Subquery(avg_rating_subquery), 0.0),
        review_count = Coalesce(Subquery(review_count_subquery), 0)
    )
    queryset = Product.objects.all()
    serializer_class = ProductListUpdateDeleteSerializer

class HashtagListCreateView(ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class HashtagUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer