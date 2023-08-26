from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'price', 'origin_price', 'name', 'description', 'barcode', 'expired_date', 'size', 'status')



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'code',)

