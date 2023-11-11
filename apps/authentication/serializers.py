from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import User


class PhoneNumberSerializer(Serializer):
    """
        phone_number uchun class
    """
    phone_number = PhoneNumberField(region="UZ")


class CodeSerializer(Serializer):
    phone_number = PhoneNumberField(region="UZ")
    code = serializers.CharField(max_length=4)


class TokenSerializer(Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)


class LoginSerializer(Serializer):
    phone_number = PhoneNumberField(region="UZ")
    password = serializers.CharField(min_length=3)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
