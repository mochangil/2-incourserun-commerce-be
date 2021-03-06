from rest_framework import serializers


from app.product.models import Product,Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
    
class ProductListCreateSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)

    #reverse relations
    hashtags = HashtagSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            'productname',
            'category',
            'description',
            'capacity',
            'price',
            'photo',
            'avg_rating',
            'review_count',
            'detailphoto',
            'created',
            'hashtags',
        )

    # def create(self, validated_data):
    #     Product.objects.create(**validated_data)
    #     return validated_data

class ProductListUpdateDeleteSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'productname',
            'category',
            'description',
            'capacity',
            'price',
            'photo',
            'avg_rating',
            'review_count',
            'detailphoto',
            'created',
        )

    def update(self,instance, validated_data):
        instance.productname = validated_data.get('productname',instance.productname)
        instance.category = validated_data.get('category',instance.category)
        instance.content = validated_data.get('content',instance.content)
        
        instance.capacity = validated_data.get('capacity',instance.capacity)
        instance.price = validated_data.get('price',instance.price)
        instance.save()

        return instance