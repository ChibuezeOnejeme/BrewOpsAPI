
from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    sku = serializers.CharField(source='product.sku', read_only=True)
    brand = serializers.CharField(source='product.brand.name', read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'product', 'brand', 'sku', 'quantity', 'total_price', 'date']
        read_only_fields = ['total_price']


