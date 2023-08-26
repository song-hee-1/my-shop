from products.models import Product
from products.serializers.basic_serializer import ProductSerializer


class ProductListQsProductSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = (*ProductSerializer.Meta.fields,)