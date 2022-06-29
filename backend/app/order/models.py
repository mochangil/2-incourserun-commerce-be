from django.db import models
from app.product.models import Product
from app.user.models import User
import datetime

class Order(models.Model):
    SHIPPING_STATE_CHOICE = (
        ('paid', '결제완료'),
        ('getready', '상품준비중'),
        ('shipping', '배송중'),
        ('complete', '배송완료')
    )
    PAY_METHOD_CHOICE = (
        ('creditcard','신용카드'),
    )
    PAY_STATUS_CHOICE = (
        ('paid','결제완료'),
        ('cancelled','결제취소')
    )
    #uid -> 결제시스템에서 주는 번호.
    #일시불 (only카드)
    user = models.ForeignKey(User, related_name="orders", on_delete = models.CASCADE)
    created = models.DateTimeField(verbose_name="주문일시", auto_now_add=True)
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    shipping_name = models.CharField(verbose_name="수령인", max_length=10)
    shipping_phone = models.CharField(verbose_name="전화번호", max_length=13)
    shipping_zipcode = models.CharField(verbose_name="우편번호", max_length=7)
    shipping_address = models.CharField(verbose_name="배송주소", max_length=1000)
    shipping_address_detail = models.CharField(verbose_name="배송상세주소", max_length=1000)
    shipping_request = models.CharField(verbose_name="배송요청사항", max_length=300, null=True, blank=True)
    shipping_status = models.CharField(verbose_name="배송상태",max_length = 10,choices=SHIPPING_STATE_CHOICE)
    pay_method = models.CharField(verbose_name="결제수단",max_length=10,choices=PAY_METHOD_CHOICE)
    pay_date = models.DateField(verbose_name="결제일자", auto_now_add=True)
    pay_status = models.CharField(verbose_name="결제상태",max_length=10,choices=PAY_STATUS_CHOICE)
    # total_number = models.ManyToManyField(many=True,)
    #프론트에서 계산.
    total_amount = models.IntegerField(verbose_name="총 상품금액")
    delivery_fee = models.IntegerField(verbose_name="배송비",null=True)
    class Meta:
        verbose_name = "주문"
        verbose_name_plural = verbose_name



class Productorder(models.Model):
    order = models.ForeignKey(Order, related_name='total_number', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="상품갯수")

    class Meta:
        verbose_name = "주문-상품"
        verbose_name_plural = verbose_name
