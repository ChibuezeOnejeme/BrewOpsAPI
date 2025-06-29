# apps/stock/serializers.py

from rest_framework import serializers
from apps.stock.models import Stock

class StockSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='product.brand.name', read_only=True)
    sku = serializers.CharField(source='product.sku', read_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'product', 'brand', 'sku', 'quantity', 'last_updated']
