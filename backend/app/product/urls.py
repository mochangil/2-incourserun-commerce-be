from django.urls import path

from .views import ProductListCreateView,ProductUpdateDeleteView

urlpatterns = [
    path("", ProductListCreateView.as_view()),
    path("/<int:pk>", ProductUpdateDeleteView.as_view()),
]
