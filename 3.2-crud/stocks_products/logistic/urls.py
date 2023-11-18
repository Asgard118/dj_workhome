from django.urls import path
from rest_framework.routers import DefaultRouter
from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    *router.urls,
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('stocks/', StockViewSet.as_view({'get': 'list'}), name='stock-list'),
]