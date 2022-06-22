from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.review.models import Review


class ReviewListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    # def create(self, validated_data):
    #     Product.objects.create(**validated_data)
    #     return validated_data

class ReviewListUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def update(self,instance, validated_data):
        instance.rating = validated_data.get('rating',instance.rating)
        instance.category = validated_data.get('category',instance.category)
        instance.context = validated_data.get('context',instance.context)
        instance.save()

        return instance