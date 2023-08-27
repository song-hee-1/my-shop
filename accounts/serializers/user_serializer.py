from rest_framework import serializers
from accounts.models import User


class UserSignUpPostSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField()


class UserLoginPostSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
