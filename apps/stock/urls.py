from django.urls import path
from .views import StockListCreateView, StockDetailView

urlpatterns = [
    path('', StockListCreateView.as_view(), name='stock-list-create'),
    path('<int:id>/', StockDetailView.as_view(), name='stock-detail'),
]
