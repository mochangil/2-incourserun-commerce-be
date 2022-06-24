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
    description = models.TextField(verbose_name="내용")
    # avg_rating, photo, detail_photo
    capacity = models.IntegerField(verbose_name="용량")
    price = models.IntegerField(verbose_name="가격")
    photo = models.CharField(verbose_name="상품사진",max_length=500,null=True)
    detailphoto = models.CharField(verbose_name="상품사진",max_length=500,null=True)
    # hashtags = models.ManyToManyField("Hashtag",related_name='product')
    created = models.DateTimeField(verbose_name="등록날짜", auto_now_add=True)

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.productname

class Hashtag(models.Model):
    name = models.CharField(verbose_name="이름",max_length=20)
    product = models.ForeignKey(Product,related_name="hashtags",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "해시태그"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name