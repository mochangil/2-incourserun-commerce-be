from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.order.models import Order


class OrderListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def create(self, validated_data):
    #     Product.objects.create(**validated_data)
    #     return validated_data

class OrderListUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'