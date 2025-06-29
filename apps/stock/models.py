
from django.db import models
from apps.products.models import Product

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True) # this can show if a sales is deleted and retunrns good for tracking criminal activities

    def __str__(self):
        return f"{self.product.brand.name} - {self.product.sku} | Qty: {self.quantity}"
