# Generated by Django 3.2.7 on 2022-06-23 14:39

import app.user.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(default='', max_length=10, unique=True, verbose_name='별칭')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='이메일')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='휴대폰')),
                ('gender', models.CharField(choices=[('M', 'Man'), ('W', 'Woman')], max_length=6, null=True, verbose_name='성별')),
                ('age', models.CharField(choices=[('10', '10s'), ('20', '20s'), ('30', '30s'), ('40', '40s'), ('50', '50s')], max_length=6, null=True, verbose_name='나이')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='주소')),
                ('zipcode', models.IntegerField(null=True, verbose_name='우편주소')),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='프로필사진')),
                ('created', models.DateField(auto_now=True, verbose_name='가입날짜')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
            },
            managers=[
                ('objects', app.user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('kakao', '카카오'), ('naver', '네이버'), ('facebook', '페이스북'), ('google', '구글'), ('apple', '애플')], max_length=16, verbose_name='타입')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '소셜',
                'verbose_name_plural': '소셜',
            },
        ),
    ]
