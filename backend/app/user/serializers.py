import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Cart, User
import string

from app.user.models import User, Social, SocialKindChoices


class UserSocialLoginSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)
    state = serializers.CharField(write_only=True)
    redirect_uri = serializers.URLField(write_only=True)

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    is_register = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        if attrs['state'] not in SocialKindChoices:
            raise ValidationError({'kind': '지원하지 않는 소셜 타입입니다.'})

        attrs['social_user_id'] = self.get_social_user_id(attrs['code'], attrs['state'])

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        social_user_id = validated_data['social_user_id']
        state = validated_data['state']
        # get_or_create
        # User.objects 메서드에 의해 생성되었다면 created = True, 기존의 데이터베이스에서 꺼내왔다면 = False
        # user에는 우리가 꺼내려고 하는 모델의 인스턴스.
        user, created = User.objects.get_or_create(email=f'{social_user_id}@{state}.social', defaults={
            'password': make_password(None),
        })

        if created:
        #새롭게 생성된 user에 대해 kakao의 정보와 연동한다.
            user.username = validated_data['kakao_account']['name']
            user.email = validated_data['kakao_account']['email']
            user.gender = 'Woman' if validated_data['kakao_account']['gender'] else 'Man'
            agematch = validated_data['kakao_account']['gender']
            if agematch == "10~19":
                user.age = "10s"
            elif agematch == "20~29":
                user.age = "20s"
            elif agematch == "30~39":
                user.age = "30s"
            elif agematch == "40~49":
                user.age = "40s"
            else:
                user.age = "50s"
            user.save()
            Social.objects.create(user=user, kind=state)

        refresh = RefreshToken.for_user(user)

        return {
            'access': refresh.access_token,
            'refresh': refresh,
            'is_register': user.is_register,
        }

    def get_social_user_id(self, code, state):
        redirect_uri = settings.SOCIAL_REDIRECT_URL
        social_user_id = getattr(self, f'get_{state}_user_id')(code, redirect_uri)
        return social_user_id

    def get_kakao_user_id(self, code, redirect_uri):
        url = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_CLIENT_ID,
            'redirect_uri': redirect_uri,
            'code': code,
            'client_secret': settings.KAKAO_CLIENT_SECRET,
        }
        response = requests.post(url=url, data=data)
        if not response.ok:
            raise ValidationError('KAKAO GET TOKEN API ERROR')
        data = response.json()

        url = 'https://kapi.kakao.com/v2/user/me'
        headers = {
            'Authorization': f'Bearer {data["access_token"]}'
        }
        response = requests.get(url=url, headers=headers)
        if not response.ok:
            raise ValidationError('KAKAO ME API ERROR')
        data = response.json()

        return data['id']

    def get_naver_user_id(self, code, redirect_uri):
        pass

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields='__all__'

    # get_or_create
    def create(self,validated_data):
        productname = validated_data["product"]
        productamounts = validated_data["amounts"]
        username = validated_data["user"]
        content,created=Cart.objects.get_or_create(product=productname,defaults=dict(user=username,amounts=productamounts))
        if created!=True:
            content.amounts += productamounts
            content.save()
        return content


class UserSerializer(serializers.ModelSerializer):
    cart = CartSerializer(many=True,read_only=True)
    class Meta:
        model=get_user_model()
        fields=['username','nickname','gender','phone','email','profile_img','age','zipcode','address','cart']
        #read_only_fields = ['username','nickname','gender','phone','email','profile_img','age','zipcode','address']

class UserUpdateDeleteSerializer(serializers.ModelSerializer):
    cart = CartSerializer(many=True, read_only=True)
    class Meta:
        model=get_user_model()
        fields=['profile_img','username','nickname','phone','email','zipcode','address','cart']
        
    def update(self, instance, validated_data):
        instance.profile_img = validated_data.get('profile_img',instance.profile_img)
        instance.username = validated_data.get('username',instance.username)
        instance.nickname = validated_data.get('nickname',instance.nickname)
        
        instance.phone = validated_data.get('phone',instance.phone)
        instance.email = validated_data.get('email',instance.email)
        instance.zipcode = validated_data.get('zipcode',instance.zipcode)
        instance.address = validated_data.get('address',instance.address)
        instance.save()
        return instance




        