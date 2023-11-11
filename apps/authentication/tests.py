from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from apps.users.models import User

# user app uchun testlar


class UserTest(TestCase):

    def setUp(self):
        self.phone_number = "+998330221211"
        self.first_name = "John"

    def test_user_creation(self):
        item = User.objects.create(
            first_name="John", phone_number=self.phone_number)
        self.assertEqual(item.first_name, self.first_name)
        self.assertEqual(item.phone_number, self.phone_number)

    def test_phone_number_registration(self):
        url = reverse('sign_up')
        data = {
            "phone_number": self.phone_number
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.json()["message"], "sms code send")

    def test_verify_code(self):
        verify_url = reverse('verify_code')
        code = cache.get(self.phone_number)
        data = {
            "phone_number": self.phone_number,
            'code': code
        }
        response = self.client.post(verify_url, data=data)
        self.assertEqual(response.status_code, 200)
