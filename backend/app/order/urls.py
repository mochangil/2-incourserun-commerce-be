from django.urls import path

from app.order.views import OrderListCreateView,OrderUpdateDeleteView, ProductorderCreateView,ProductorderUpdateDeleteView

urlpatterns = [
    path("", OrderListCreateView.as_view()),
    path("/<int:pk>", OrderUpdateDeleteView.as_view()),
    path("/productorder",ProductorderCreateView.as_view()),
    path("/productorder/<int:pk>",ProductorderUpdateDeleteView.as_view()),
]
