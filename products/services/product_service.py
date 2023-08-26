from accounts.models import User
from core.utils.base_service import BaseService
from core.utils.paginate import CursorPagination
from products.models import Product, ProductStatusType
from products.serializers.product_serializer import ProductListQsProductSerializer, ProductRetrieveQsProductSerializer


class ProductService(BaseService):

    def __init__(self, user=None):
        self._user = user

    def list(self, request):
        products = Product.objects.filter(
           user=self.user, status=ProductStatusType.REGISTERED.value
        )
        pagination = CursorPagination()
        paginated_products = pagination.paginate_queryset(products, request)

        serializer = ProductListQsProductSerializer(paginated_products, many=True)

        pagination_data = {
            'next': pagination.get_next_link(),
            'previous': pagination.get_previous_link(),
            'results': serializer.data,
        }

        return pagination_data

    def retrieve(self, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Exception('ProductService.retrieve: Product does not exist')

        if product.user != self.user:
            raise Exception('ProductService.retrieve: No Permission')

        product = Product.objects.filter(
            id=id,
            status=ProductStatusType.REGISTERED.value
        ).prefetch_related(
            'categories'
        )

        serializer = ProductRetrieveQsProductSerializer(product, many=True)
        return serializer.data

    def delete(self, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Exception('ProductService.retrieve: Product does not exist')

        if product.user != self.user:
            raise Exception('ProductService.retrieve: No Permission')

        product.status = ProductStatusType.DELETED.value
        product.save()

    @property
    def user(self) -> User:
        return self._user
