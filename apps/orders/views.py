from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from apps.orders.models import Contact
from apps.orders.serializers import ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    model = Contact
    serializer_class = ContactSerializer
