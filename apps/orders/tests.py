from django.test import TestCase
from django.urls import reverse


class UserTest(TestCase):

    def setUp(self):
        self.phone_number = "+998905360968"
        self.first_name = "John"

    def test_phone_number_registration(self):
        url = reverse('contact_create')
        data = {
            "phone_number": self.phone_number,
            'first_name': self.first_name
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
