from django.urls import path

from .views import ReplyListCreateView, ReplyUpdateDeleteView, ReviewListCreateView,ReviewUpdateDeleteView

urlpatterns = [
    path("", ReviewListCreateView.as_view()),
    path("/<int:pk>", ReviewUpdateDeleteView.as_view()),
    path("/reply",ReplyListCreateView.as_view()),
    path("/reply/<int:pk>",ReplyUpdateDeleteView.as_view()),
]
