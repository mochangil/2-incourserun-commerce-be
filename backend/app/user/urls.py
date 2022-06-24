from django.urls import path

from app.user.views import *

urlpatterns = [
    path('', UserListCreateView.as_view()),
    # 생성된 유저정보의 세부사항 입력으로 이동.
    #회원정보수정
    # path('/usercreate',UserListCreateView.as_view()),
    path('/<int:pk>', UserUpdateDeleteView.as_view()),
    path('/cart', CartListCreateView.as_view()),
    path('/cart/<int:pk>', CartUpdateDeleteView.as_view()),
    path('/social_login', UserSocialLoginView.as_view()),
    # path('social_login/info/', UserCreateView.as_vieew())
    path('/login/kakao',kakao_login),
    path('/login/kakao/callback', kakao_callback)
]