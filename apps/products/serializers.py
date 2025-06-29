from rest_framework import serializers
from .models import  Product


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'brand', 'brand_name', 'sku', 'price', 'image','created_at']
