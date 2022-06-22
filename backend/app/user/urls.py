from django.urls import path

from app.user.views import *

urlpatterns = [
    path('', UserListView.as_view()),
    # 생성된 유저정보의 세부사항 입력으로 이동.
    path('/<int:pk>', UserUpdateDeleteView.as_view()),
    # 카카오로그인을 첫번째로, 유저생성후 카카오정보와 연동
    path('/social_login', UserSocialLoginView.as_view()),
    # path('social_login/info/', UserCreateView.as_vieew())
]