from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product
from products.serializers.product_serializer import ProductListQsProductSerializer
from products.services.product_service import ProductService


class ProductViewSet(viewsets.GenericViewSet):
    serializer_class = ProductListQsProductSerializer
    queryset = Product.objects.all()

    def list(self, request: Request):
        service = ProductService(user=request.user)
        output_dto = service.list(request)
        return Response(output_dto)

    def retrieve(self, request: Request, pk):
        id = int(pk)
        service = ProductService(user=request.user)
        output_dto = service.retrieve(id=id)
        return Response(output_dto)


