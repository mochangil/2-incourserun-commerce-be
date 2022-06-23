from django.urls import path, include

urlpatterns = [
    path("example", include("app.example.urls")),
    path("user", include("app.user.urls")),
    path("products", include("app.product.urls")),
    path("reviews", include("app.review.urls")),
    path("orders", include("app.order.urls")),
    path("cart",include("app.cart.urls")),
]
