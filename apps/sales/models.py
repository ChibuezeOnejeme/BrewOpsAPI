from django.db import models
from django.core.exceptions import ValidationError
from apps.products.models import Product
from apps.stock.models import Stock  # Ensure this model exists

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        stock = Stock.objects.get(product=self.product)

        if self.pk:
            # Updating existing sale
            old_sale = Sale.objects.get(pk=self.pk)
            quantity_diff = self.quantity - old_sale.quantity
        else:
            # Creating new sale
            quantity_diff = self.quantity

        if quantity_diff > stock.quantity:
            raise ValidationError("Not enough stock to fulfill this sale.")

        stock.quantity -= quantity_diff
        stock.save()

        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Restore stock before deletion
        stock = Stock.objects.get(product=self.product)
        stock.quantity += self.quantity
        stock.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.product.brand.name} - {self.product.sku} ({self.quantity}) = {self.total_price}"
