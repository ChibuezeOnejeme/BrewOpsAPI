from rest_framework import mixins, generics
from .models import Stock
from .serializers import StockSerializer
from drf_yasg.utils import swagger_auto_schema

class StockListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    @swagger_auto_schema(tags=["Stock"])
    def get(self, request): 
        return self.list(request)
    
    @swagger_auto_schema(tags=["Stock"])
    def post(self, request): 
        return self.create(request)


class StockDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "id"

    @swagger_auto_schema(tags=["Stock"])
    def get(self, request, *args, **kwargs): 
        return self.retrieve(request)
    
    @swagger_auto_schema(tags=["Stock"])
    def put(self, request, *args, **kwargs): 
        return self.update(request)
    
    @swagger_auto_schema(tags=["Stock"])
    def patch(self, request, *args, **kwargs): 
        return self.partial_update(request)
    
    @swagger_auto_schema(tags=["Stock"])
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request)
