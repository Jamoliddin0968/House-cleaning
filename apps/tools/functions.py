
import random

import jwt
from rest_framework.exceptions import ValidationError

# from apps.users.models import VerifyCode


def authenticate_token(request):
    """
        return VerfifyCode object from token
    """
    pass
    # auth_header = request.META.get('HTTP_AUTHORIZATION')
    # try:
    #     token = jwt.decode(auth_header, VERIFY_SECRET_KEY,
    #                        algorithms=["HS256"])
    #     id = token.get("id")
    #     if id:
    #         obj = VerifyCode.objects.get(id=id)
    #         return obj
    #     raise ValidationError("Invalid token")
    # except:
    #     raise ValidationError("Invalid token")


def create_code():
    code = "".join([str(random.randint(0, 100) % 10) for _ in range(4)])
    return code


def send_sms(phone_number, code):

    return True
