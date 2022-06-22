from django.urls import path

from app.order.views import OrderListCreateView,OrderUpdateDeleteView

urlpatterns = [
    path("", OrderListCreateView.as_view()),
    path("/<int:pk>", OrderUpdateDeleteView.as_view()),
]
