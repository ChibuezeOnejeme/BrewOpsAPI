from rest_framework import mixins, generics
from .models import Sale
from .serializers import SaleSerializer
from drf_yasg.utils import swagger_auto_schema

class SaleListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    @swagger_auto_schema(tags=["Sales"])
    def get(self, request): 
        return self.list(request)
    @swagger_auto_schema(tags=["Sales"])
    def post(self, request): 
        return self.create(request)


class SaleDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = "id"

    @swagger_auto_schema(tags=["Sales"])
    def get(self, request, *args, **kwargs): 
        return self.retrieve(request)
    
    @swagger_auto_schema(tags=["Sales"])
    def put(self, request, *args, **kwargs): 
        return self.update(request)
    
    @swagger_auto_schema(tags=["Sales"])
    def patch(self, request, *args, **kwargs): 
        return self.partial_update(request)
    
    @swagger_auto_schema(tags=["Sales"])
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request)
