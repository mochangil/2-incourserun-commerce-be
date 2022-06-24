from django.urls import path

from .views import ProductListCreateView,ProductUpdateDeleteView,HashtagListCreateView,HashtagUpdateDeleteView

urlpatterns = [
    path("", ProductListCreateView.as_view()),
    path("/<int:pk>", ProductUpdateDeleteView.as_view()),
    path("hashtag",HashtagListCreateView.as_view()),
    path("hashtag/<int:pk>",HashtagUpdateDeleteView.as_view())
]
