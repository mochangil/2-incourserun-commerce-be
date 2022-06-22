from collections import UserList
from rest_framework.generics import CreateAPIView,ListAPIView,GenericAPIView
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin

from app.user.serializers import *


class UserSocialLoginView(CreateAPIView):
    """
    유저 소셜로그인
    ---
    소셜로그인의 callback으로 전달받은 code와 state값으로 로그인 또는 회원가입을 합니다.
    """
    serializer_class = UserSocialLoginSerializer

class UserListView(CreateAPIView):
    """
    회원목록 확인
    """
    user = get_user_model()
    queryset=user.objects.all()
    serializer_class = UserListSerializer

class UserUpdateDeleteView(GenericAPIView,UpdateModelMixin,DestroyModelMixin):
    """
    회원 update&Delete
    """
    user = get_user_model()
    queryset=user.objects.all()
    serializer_class = UserUpdateDeleteSerializer

