from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.serializers.user_serializer import UserLoginPostSerializer, UserSignUpPostSerializer
from accounts.services.user_service import UserService
from core.utils.permission import IsNotAuthenticated


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserLoginPostSerializer

    @action(methods=['POST'], detail=False, permission_classes=[IsNotAuthenticated])
    def signup(self, request: Request):
        serializer = UserSignUpPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = UserService()
        output_dto = service.signup(
            phone=serializer.validated_data['phone'],
            password=serializer.validated_data['password']
        )
        return Response(output_dto)

    @action(methods=['POST'], detail=False, permission_classes=[IsNotAuthenticated])
    def login(self, request: Request):
        serializer = UserLoginPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = UserService()
        output_dto = service.login(
            phone=serializer.validated_data['phone'],
            password=serializer.validated_data['password']
        )
        return Response(output_dto)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request: Request):
        logout(request)
        return Response()

