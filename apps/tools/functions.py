
import random
import threading

from decouple import config
from eskiz.client import SMSClient

# from apps.users.models import VerifyCode


def create_code():
    code = "".join([str(random.randint(0, 100) % 10) for _ in range(4)])
    return code


email = config('email', '')
pswd = config('password', '')
client = SMSClient(
    api_url="https://notify.eskiz.uz/api/",
    email=email,
    password=pswd,
)


def add_contact(phone_number, name):
    contact, _ = Contact.objects.get_or_create(phone_number=phone_number)
    if _:
        client._add_sms_contact(
            first_name=name,
            phone_number=phone_number,
            group="Garden"
        )


def get_sms_content(code):
    msg = f"""Tasdiqlash kodi {code}"""
    return msg


def send_sms_code(phone_number, code):
    phone_number = phone_number.replace('+', '')
    message = get_sms_content(code=code)
    res = client._send_sms(
        phone_number=phone_number, message=message
    )
    return True


def send_sms(phone_number, code):
    sms_thread = threading.Thread(
        target=send_sms_code, args=(phone_number, code))
    sms_thread.start()
    sms_thread.join()
    return True
