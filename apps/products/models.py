from django.db import models
from apps.brands.models import Brand


SEGMENT_CHOICES = [
    ("Lager", "Lager"),
    ("Stout", "Stout"),
    ("Malt", "Malt"),
    ("Rtd", "Rtd"),
]

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50)  # e.g. "600ml bottle"
    product_type = models.CharField(max_length=20, choices=SEGMENT_CHOICES, default="Lager")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # ← Add this
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('brand', 'sku')

    def __str__(self):
        return f"{self.brand.name} - {self.sku}"
