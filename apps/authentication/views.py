from django.contrib.auth import authenticate
from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers import (CodeSerializer, LoginSerializer,
                                             PhoneNumberSerializer,
                                             TokenSerializer)
from apps.tools.functions import create_code, send_sms
from apps.users.models import User


class PhoneNumberAuthAPIView(GenericAPIView):
    serializer_class = PhoneNumberSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        phone_number = data.validated_data.get('phone_number').as_e164
        registration_code = create_code()
        cache.set(phone_number, registration_code, timeout=60*2)
        send_sms(phone_number=phone_number, code=registration_code)
        return Response({"message": "sms code send"}, status=200)


class VerifyCodeAPIView(APIView):
    def post(self, request):
        data = CodeSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        phone_number = data.validated_data.get('phone_number').as_e164
        code = data.validated_data.get('code')
        verify_code = cache.get(phone_number)
        if verify_code:
            if code == verify_code:
                user, _ = User.objects.get_or_create(phone_number=phone_number)
                tokens = user.tokens()
                data = TokenSerializer(tokens).data
                return Response(data=data, status=200)
            else:
                raise ValidationError({"message": "Parol xato kiritildi"})
        raise ValidationError({"message": "Parol eskirgna"})


class LoginAPIView(APIView):

    def post(self, request):
        data = LoginSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        phone_number = data.validated_data.get('phone_number')
        password = data.validated_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if user:
            return Response({"error": "Incorrect phone number or password"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            tokens = user.tokens()
            data = TokenSerializer(tokens).data
            return Response(data=data, status=200)
