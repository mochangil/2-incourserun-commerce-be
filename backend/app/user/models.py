from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from app.product.models import Product
from django.core.validators import MinValueValidator

class UserManager(DjangoUserManager):
    def _create_user(self, username, password=None, **extra_fields):
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    # CHOICES?
    GENDER_CHOICES = [
        ('M','Man'),
        ('W','Woman'),
    ]
    AGE_CHOICES = [
        ('10','10s'),
        ('20','20s'),
        ('30','30s'),
        ('40','40s'),
        ('50','50s'),
    ]
    first_name = None
    last_name = None
    nickname = models.CharField(verbose_name="별칭", max_length=10,null=True,default="")
    email = models.EmailField(verbose_name="이메일",unique=True)
    real_email=models.EmailField(verbose_name="실제이메일",null=True)
    phone = models.CharField(verbose_name="휴대폰", max_length=11, null=True, blank=True)
    gender = models.CharField(verbose_name="성별",max_length = 6,choices=GENDER_CHOICES,null=True)
    age = models.CharField(verbose_name="나이",max_length = 6,choices=AGE_CHOICES,null=True)
    address = models.CharField(verbose_name="주소",max_length = 100,null=True)
    zipcode = models.IntegerField(verbose_name="우편주소",null=True)
    profile_img = models.ImageField(verbose_name="프로필사진",blank=True,null=True)
    created = models.DateField(verbose_name="가입날짜",auto_now=True)
    is_register = models.BooleanField(verbose_name="등록여부",default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class SocialKindChoices(models.TextChoices):
    KAKAO = 'kakao', '카카오'
    NAVER = 'naver', '네이버'
    FACEBOOK = 'facebook', '페이스북'
    GOOGLE = 'google', '구글'
    APPLE = 'apple', '애플'


class Social(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    kind = models.CharField(verbose_name='타입', max_length=16, choices=SocialKindChoices.choices)

    class Meta:
        verbose_name = '소셜'
        verbose_name_plural = verbose_name

#manytomany 쓰로트
#중간테이블

class Cart(models.Model):
    user = models.ForeignKey(User,related_name="cart",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amounts = models.IntegerField(verbose_name="수량")

    class Meta:
        verbose_name = "장바구니"
        verbose_name_plural = verbose_name
