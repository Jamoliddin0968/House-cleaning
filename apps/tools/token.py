from datetime import timedelta

import jwt
from django.utils import timezone
from rest_framework_simplejwt.tokens import Token
VERIFY_SECRET_KEY = "aessecretauthkey"
CODE_EXPIRE = 5
from rest_framework_simplejwt.tokens import AccessToken
from drf_standardized_errors.handler import exception_handler
from rest_framework_simplejwt.authentication import  JWTAuthentication
class SignUpToken():

    @classmethod
    def get_token(cls,obj):
        current_time = timezone.now()
        _token = jwt.encode({"id": str(obj.id), "time": str(current_time)}, VERIFY_SECRET_KEY, algorithm="HS256")
        return _token

class MyToken(Token):
    token_type = "access"
    lifetime = timedelta(days=1)