from django.urls import path, include

urlpatterns = [
    path("example", include("app.example.urls")),
    path("user", include("app.user.urls")),
    path("product", include("app.product.urls")),
    path("review", include("app.review.urls")),
    path("order", include("app.order.urls")),
]
