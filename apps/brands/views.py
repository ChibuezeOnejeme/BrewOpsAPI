from rest_framework import generics, mixins
from .models import Brand
from .serializers import BrandSerializer
from drf_yasg.utils import swagger_auto_schema

class BrandListCreateView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @swagger_auto_schema(tags=["Brands"])
    def get(self, request): 
        return self.list(request)
    
    @swagger_auto_schema(tags=["Brands"])
    def post(self, request): 
        return self.create(request)


class BrandDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = "id"
    @swagger_auto_schema(tags=["Brands"])
    def get(self, request, *args, **kwargs): 
        return self.retrieve(request)
    
    @swagger_auto_schema(tags=["Brands"])
    def put(self, request, *args, **kwargs): 
        return self.update(request)
    
    @swagger_auto_schema(tags=["Brands"])
    def patch(self, request, *args, **kwargs): 
        return self.partial_update(request)
    
    @swagger_auto_schema(tags=["Brands"])
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request)
