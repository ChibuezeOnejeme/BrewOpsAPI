from django.urls import path
from .views import SaleListCreateView, SaleDetailView

urlpatterns = [
    path('', SaleListCreateView.as_view(), name='sale-list-create'),
    path('<int:id>/', SaleDetailView.as_view(), name='sale-detail'),
]
