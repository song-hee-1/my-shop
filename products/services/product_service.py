from accounts.models import User
from core.utils.base_service import BaseService
from core.utils.paginate import CursorPagination
from products.models import Product
from products.serializers.product_serializer import ProductListQsProductSerializer


class ProductService(BaseService):

    def __init__(self, user=None):
        self._user = user

    def list(self, request):
        products = Product.objects.filter(
           user=self.user
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

    @property
    def user(self) -> User:
        return self._user
