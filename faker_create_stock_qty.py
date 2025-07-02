import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
django.setup()

from apps.products.models import Product
from apps.stock.models import Stock

# Clear existing stock (optional)
Stock.objects.all().delete()

products = Product.objects.all()
count = 0

for product in products:
    quantity = random.randint(50, 500)  # Random initial stock level
    Stock.objects.create(product=product, quantity=quantity)
    count += 1

print(f"✅ Populated stock for {count} products.")
