from django.contrib import admin
from app.user.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = [
        ('User information', {'fields': ['username','nickname','email','phone','gender','age',
        'address','zipcode','profile_img']})
    ]

    list_display = (
        "username",
        'username',
        'nickname',
        'email',
        'phone',
        'gender',
        'age',
        'address',
        'zipcode',
        'profile_img'
    )