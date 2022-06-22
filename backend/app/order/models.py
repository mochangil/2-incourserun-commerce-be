from operator import mod
from django.db import models
from app.product.models import Product
from app.user.models import User

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    #product count
    #deliveryfee -> True = 3000, False = free
    deliveryfee=models.BooleanField(verbose_name="배달비",default=True)
    zipcode = models.IntegerField(verbose_name="우편번호",null=True)
    address = models.CharField(verbose_name="주소",null=True)
    orderdate=models.DateTimeField(verbose_name="주문시간정보",auto_now=True)

    class Meta:
        verbose_name = "주문"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name