from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.serializers import ModelSerializer

from apps.orders.models import Contact


class ContactSerializer(ModelSerializer):
    phone_number = PhoneNumberField(region="UZ")

    class Meta:
        model = Contact
        fields = "__all__"
