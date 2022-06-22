# from pyexpat import model
# from termios import VERASE
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('BATH&SHAMPOO', '바스&샴푸'),
        ('LOTION', '파우더로션'),
        ('OIL', '오일'),
        ('CREAM', '크림')
    ]
    #id = models.IntegerField(verbose_name="고유번호")
    productname = models.CharField(verbose_name="제품명", max_length=256)
    category = models.CharField(verbose_name ="category",max_length=20,choices=CATEGORY_CHOICES)
    content = models.TextField(verbose_name="내용")
    # avg_rating, photo, detail_photo
    capacity = models.IntegerField(verbose_name="용량")
    price = models.IntegerField(verbose_name="가격")
    created = models.DateTimeField(verbose_name="등록날짜", auto_now_add=True)

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.productname