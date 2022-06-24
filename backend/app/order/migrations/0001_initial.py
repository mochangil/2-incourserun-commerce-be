# Generated by Django 3.2.7 on 2022-06-24 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0005_hashtag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='주문일시')),
                ('shipping_name', models.CharField(max_length=10, verbose_name='수령인')),
                ('shipping_phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('shipping_zipcode', models.CharField(max_length=7, verbose_name='우편번호')),
                ('shipping_address', models.CharField(max_length=1000, verbose_name='배송주소')),
                ('shipping_address_detail', models.CharField(max_length=1000, verbose_name='배송상세주소')),
                ('shipping_request', models.CharField(blank=True, max_length=300, null=True, verbose_name='배송요청사항')),
                ('shipping_status', models.CharField(choices=[('paid', '결제완료'), ('getready', '상품준비중'), ('shipping', '배송중'), ('complete', '배송완료')], max_length=10, verbose_name='배송상태')),
                ('pay_method', models.CharField(choices=[('creditcard', '신용카드')], max_length=10, verbose_name='결제수단')),
                ('pay_date', models.DateField(auto_now_add=True, verbose_name='결제일자')),
                ('pay_status', models.CharField(choices=[('paid', '결제완료'), ('cancelled', '결제취소')], max_length=10, verbose_name='결제상태')),
                ('total_amount', models.IntegerField(verbose_name='총 상품금액')),
                ('delivery_fee', models.IntegerField(null=True, verbose_name='배송비')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
            },
        ),
        migrations.CreateModel(
            name='Productorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='상품갯수')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_number', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '주문-상품',
                'verbose_name_plural': '주문-상품',
            },
        ),
    ]
