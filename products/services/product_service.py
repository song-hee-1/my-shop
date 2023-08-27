from django.db.models import Q

from accounts.models import User
from core.utils.base_service import BaseService
from core.utils.exception import DoesNotExists, NoPermission
from core.utils.initials import get_initials
from core.utils.paginate import CursorPagination
from products.models import Product, ProductStatusType, ProductCategory
from products.serializers.product_serializer import ProductListQsProductSerializer, ProductUpdatePostSerializer, \
    ProductRetrieveQsProductSerializer


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

    def create(self, data):
        data['name_initials'] = get_initials(data['name'])
        categories_data = data.pop('categories')
        product = Product.objects.create(**data, user=self.user)

        for category_data in categories_data:
            category_instance, created = ProductCategory.objects.get_or_create(**category_data)
            product.categories.add(category_instance)

        serializer = ProductRetrieveQsProductSerializer(product)
        return serializer.data

    def retrieve(self, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise DoesNotExists()

        if product.user != self.user:
            raise NoPermission()

        product = Product.objects.filter(
            id=id,
            status=ProductStatusType.REGISTERED.value
        ).prefetch_related(
            'categories'
        ).first()

        serializer = ProductRetrieveQsProductSerializer(product)
        return serializer.data

    def delete(self, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise DoesNotExists()

        if product.user != self.user:
            raise NoPermission()

        product.status = ProductStatusType.DELETED.value
        product.save()

    def update(self, id, data):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise DoesNotExists()

        if product.user != self.user:
            raise NoPermission()

        fields_to_update = [
            'price', 'origin_price', 'name', 'description', 'barcode',
            'expired_date', 'size', 'status'
        ]

        for field in fields_to_update:
            if field in data:
                setattr(product, field, data[field])

        product.save()

        categories_data = data.pop('categories', [])
        product.categories.clear()

        for category_data in categories_data:
            category_instance, _ = ProductCategory.objects.get_or_create(**category_data)
            product.categories.add(category_instance)

        return ProductUpdatePostSerializer(product).data

    def search(self, keyword):
        keyword_initials = get_initials(keyword)
        products = Product.objects.filter(
            Q(user=self.user) &
            Q(status=ProductStatusType.REGISTERED.value) &
            Q(name__icontains=keyword) | Q(name_initials__icontains=keyword_initials)
        )

        serializer = ProductListQsProductSerializer(products, many=True)
        return serializer.data

    @property
    def user(self) -> User:
        if self._user is None or self._user.is_anonymous:
            raise NoPermission()
        return self._user
