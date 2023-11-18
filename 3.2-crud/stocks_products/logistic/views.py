from rest_framework import viewsets
from django.db.models import Q
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        return queryset

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        queryset = Stock.objects.all()
        product_id = self.request.query_params.get('product_id', None)
        if product_id:
            queryset = queryset.filter(positions__product__id=product_id)
        return queryset
