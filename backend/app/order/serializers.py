from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.order.models import Order,Productorder
from app.product.serializers import ProductListCreateSerializer

class ProductorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productorder
        fields = '__all__'

class OrderListCreateSerializer(serializers.ModelSerializer):
    total_number = ProductorderSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = (
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
            'total_number',
            'total_amount',
            'delivery_fee',

        )

    # def create(self, validated_data):
    #     Product.objects.create(**validated_data)
    #     return validated_data

class OrderListUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

