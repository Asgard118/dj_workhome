from rest_framework import serializers
from .models import Product, StockProduct, Stock

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

class StockProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = StockProductSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position_data in positions_data:
            product_data = position_data.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            StockProduct.objects.create(stock=stock, product=product, **position_data)

        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        # Удаляем все связанные продукты на складе
        instance.positions.all().delete()

        for position_data in positions_data:
            product_data = position_data.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            StockProduct.objects.create(stock=stock, product=product, **position_data)

        return stock