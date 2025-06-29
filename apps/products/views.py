from rest_framework import generics, mixins
from .models import  Product
from .serializers import  ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.request import Request
from rest_framework.response import Response

class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"







class ProductListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "sku", "brand","created_at"]# localhost:8000/posts/posts_for/?title= any

    queryset = Product.objects.all()
    
    @swagger_auto_schema(tags=["Products"])
    def get(self, request): 
        return self.list(request)
    
    @swagger_auto_schema(tags=["Products"],operation_description="Name field should be either of these Lager,Stout,Malt")
    def post(self, request): 
        return self.create(request)


class ProductDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
    
    @swagger_auto_schema(tags=["Products"])
    def get(self, request, *args, **kwargs): 
        return self.retrieve(request)
    
    @swagger_auto_schema(tags=["Products"])
    def put(self, request, *args, **kwargs): 
        return self.update(request)
    
    @swagger_auto_schema(tags=["Products"])
    def patch(self, request, *args, **kwargs): 
        return self.partial_update(request)
    
    @swagger_auto_schema(tags=["Products"])
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request)

