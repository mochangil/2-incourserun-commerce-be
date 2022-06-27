from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product information', {'fields': [
            'productname',
            'category',
            'description',
            'capacity',
            'price',
            'photo',
            'detailphoto',
        ]})
    ]

    list_display = (
        'productname',
        'category',
        'description',
        'capacity',
        'price',
        'photo',
        'detailphoto',
        'created',
    )