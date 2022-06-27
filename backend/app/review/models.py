from pyexpat import model
from tabnanny import verbose
from django.db import models
from app.product.models import Product
from app.user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.FloatField(verbose_name="평점",validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    context = models.TextField(verbose_name="후기내용")
    create_date = models.DateTimeField(verbose_name="작성일자",auto_now_add=True)

    class Meta:
        #기본 정렬값 - 최신순
        ordering = ['create_date']
        verbose_name = "후기"
        verbose_name_plural = verbose_name
    
    

class Reply(models.Model):
    review = models.ForeignKey(Review,related_name="reply",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="replyuser",on_delete=models.CASCADE)
    context = models.CharField(verbose_name="내용",max_length=256)
    created = models.DateTimeField(verbose_name="작성일자", auto_now_add=True)
    #reply
    class Meta:
        verbose_name = "답글"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.context
