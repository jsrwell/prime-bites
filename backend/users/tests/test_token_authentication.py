"""
Teste Token Authentication
"""
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from users.models import User

# AUTH_URL = reverse('user:token')


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_authenticate_user_success(self):
        """
        Test authenticating a user with valid credentials.
        """
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }

        response = self.client.post(reverse('user:token'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_authenticate_user_invalid_credentials(self):
        """
        Test authenticating a user with invalid credentials.
        """
        data = {
            'email': self.user_data['email'],
            'password': 'incorrect_password',
        }

        response = self.client.post(reverse('user:token'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_authenticate_user_missing_credentials(self):
        """
        Test authenticating a user with missing credentials.
        """
        data = {
            'email': self.user_data['email'],
        }

        response = self.client.post(reverse('user:token'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
