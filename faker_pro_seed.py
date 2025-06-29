import os
import django
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")  # update to match your project
django.setup()

from apps.brands.models import Brand
from apps.products.models import Product

# Clear existing data (optional)
Brand.objects.all().delete()
Product.objects.all().delete()

brands_and_skus = {
    "Budweiser": [("600ml Bottle", "Lager"), ("330ml Can", "Lager")],
    "Hero Lager": [("600ml Bottle", "Lager"), ("330ml Bottle", "Lager")],
    "Trophy": [("600ml Bottle", "Lager"), ("500ml Can", "Lager")],
    "Eagle Lager": [("600ml Bottle", "Lager"), ("330ml Can", "Lager")],
    "Beta Malt": [("330ml Bottle", "Malt"), ("300ml Can", "Malt")],
    "Eagle Stout": [("600ml Bottle", "Stout"), ("330ml Can", "Stout")],
}

for brand_name, skus in brands_and_skus.items():
    brand = Brand.objects.create(
        name=brand_name,
        description=f"{brand_name} is a popular Nigerian beverage by AB InBev."
    )

    for sku, segment in skus:
        price = Decimal("350.00") if "330ml" in sku else Decimal("500.00")
        Product.objects.create(
            brand=brand,
            sku=sku,
            product_type=segment,
            price=price,
        )

print("✅ AB InBev Nigeria brands and products seeded successfully.")
