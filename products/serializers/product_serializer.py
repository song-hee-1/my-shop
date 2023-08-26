from products.models import Product
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
