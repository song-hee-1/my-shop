from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product
from products.serializers.product_serializer import ProductListQsProductSerializer, ProductUpdatePostSerializer
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

    def delete(self, request: Request, pk):
        id = int(pk)
        service = ProductService(user=request.user)
        output_dto = service.delete(id=id)
        return Response(output_dto)

    def update(self, request: Request, pk):
        id = int(pk)
        serializer = ProductUpdatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = ProductService(user=request.user)
        output_dto = service.update(id=id, data=serializer.validated_data)
        return Response(output_dto)
