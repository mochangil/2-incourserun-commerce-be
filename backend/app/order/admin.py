from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Order information', {'fields': [
            'user',
            'created',
            'shipping_name',
            'shipping_phone',
            'shipping_zipcode',
            'shipping_address',
            'shipping_address_detail',
            'shipping_request',
            'shipping_status',
            'pay_method',
            'pay_date',
            'pay_status',
            'delivery_fee',
        ]})
    ]

    list_display = (
        'user',
        'created',
        'shipping_name',
        'shipping_phone',
        'shipping_zipcode',
        'shipping_address',
        'shipping_address_detail',
        'shipping_request',
        'shipping_status',
        'pay_method',
        'pay_date',
        'pay_status',
        'delivery_fee',
    )