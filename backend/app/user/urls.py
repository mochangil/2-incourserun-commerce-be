from django.urls import path

from app.user.views import *

urlpatterns = [
    path('social_login/', UserSocialLoginView.as_view()),
    # path('social_login/info/', UserCreateView.as_vieew())
]