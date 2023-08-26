from rest_framework import serializers

from core.utils.choice import get_choices
from products.models import Product, ProductCategory, ProductSizeType, ProductStatusType
from products.serializers.basic_serializer import ProductSerializer, ProductCategorySerializer


class ProductListQsProductSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = (*ProductSerializer.Meta.fields,)


class ProductRetrieveQsProductSerializer(ProductSerializer):
    categories = ProductCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (*ProductSerializer.Meta.fields, 'categories',)


class ProductCategoryUpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        exclude = ('id',)


class ProductUpdatePostSerializer(serializers.Serializer):
    price = serializers.IntegerField(required=False)
    origin_price = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    barcode = serializers.CharField(required=False)
    expired_date = serializers.DateField(required=False)
    size = serializers.ChoiceField(choices=get_choices(ProductSizeType), required=False)
    status = serializers.ChoiceField(choices=get_choices(ProductStatusType), required=False)
    categories = ProductCategoryUpdatePostSerializer(many=True, required=False)
