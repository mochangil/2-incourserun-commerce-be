# Generated by Django 3.2.7 on 2022-06-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=256, verbose_name='제품명')),
                ('category', models.CharField(choices=[('BATH&SHAMPOO', '바스&샴푸'), ('LOTION', '파우더로션'), ('OIL', '오일'), ('CREAM', '크림')], max_length=20, verbose_name='category')),
                ('content', models.TextField(verbose_name='내용')),
                ('capacity', models.IntegerField(verbose_name='용량')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('photo', models.CharField(max_length=500, null=True, verbose_name='상품이미지')),
                ('detailphoto', models.CharField(max_length=500, null=True, verbose_name='상품상세이미지')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='등록일시')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
            },
        ),
    ]
