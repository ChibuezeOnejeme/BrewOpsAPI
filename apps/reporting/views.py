from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from apps.sales.models import Sale
from apps.products.models import Product
from drf_yasg.utils import swagger_auto_schema


class TopSellingProductsView(APIView):
    @swagger_auto_schema(tags=["Reporting"])
    def get(self, request):
        top_products = (
            Sale.objects
            .values('product__brand__name', 'product__sku')
            .annotate(total_quantity=Sum('quantity'), total_sales=Sum('total_price'))
            .order_by('-total_quantity')[:5]
        )

        return Response(top_products, status=status.HTTP_200_OK)
