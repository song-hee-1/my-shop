from rest_framework import serializers
from accounts.models import User


class UserSignUpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password']


class UserLoginPostSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()