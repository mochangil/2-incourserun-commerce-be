from rest_framework.generics import CreateAPIView

from app.user.serializers import UserSocialLoginSerializer


class UserSocialLoginView(CreateAPIView):
    """
    유저 소셜로그인
    ---
    소셜로그인의 callback으로 전달받은 code와 state값으로 로그인 또는 회원가입을 합니다.
    """
    serializer_class = UserSocialLoginSerializer

# class UserCreateView(CreateAPIView):
#     """
#     소셜로그인 이후의 정보를 가지고 추가적인 회원정보를 입력받는다.
#     """
#     serializer_class = UserCreateSeril