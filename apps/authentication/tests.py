from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from apps.authentication.models import CustomUser as User


class CustomAuthTokenTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.valid_payload = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.invalid_payload = {
            'username': 'testuser2',
            'password': ''
        }

    def test_custom_auth_token_success(self):
        response = self.client.post('/authentication/token/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_custom_auth_token_invalid_credentials(self):
        response = self.client.post('/authentication/token/', self.invalid_payload)
        print("\n..............\n\n\n")
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
