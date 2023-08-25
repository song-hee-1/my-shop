from rest_framework import serializers


class UserSignUpPostSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()


class UserLoginPostSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
