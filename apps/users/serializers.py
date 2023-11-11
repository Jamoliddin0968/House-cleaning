from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        fields = (
            "first_name", "last_name", "phone_number", 'photo'
        )
        model = User
