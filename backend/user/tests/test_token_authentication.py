"""
Teste Token Authentication
"""
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from user.models import User


URL_TOKEN_PAIR = reverse('user:token_obtain_pair')


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        self.data_ok = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }
        self.data_invalid = {
            'email': self.user_data['email'],
            'password': 'incorrect_password',
        }
        self.data_missing = {
            'email': self.user_data['email'],
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_authenticate_user_success_HTTP_200_OK(self):
        """Test authenticating a user with valid credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_ok, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticate_user_success_access_token_received(self):
        """Test authenticating a user with valid credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_ok, format='json')
        self.assertIn('access', response.data)

    def test_authenticate_user_success_refresh_token_received(self):
        """Test authenticating a user with valid credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_ok, format='json')
        self.assertIn('refresh', response.data)

    def test_authenticate_user_invalid_credentials_HTTP_401_unauthorized(self):
        """Test authenticating a user with invalid credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_invalid, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticate_user_invalid_credentials_access_token_not_received(self):  # noqa E501
        """Test authenticating a user with invalid credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_invalid, format='json')
        self.assertNotIn('access', response.data)

    def test_authenticate_user_invalid_credentials_refresh_token_not_received(self):  # noqa E501
        """Test authenticating a user with invalid credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_invalid, format='json')
        self.assertNotIn('refresh', response.data)

    def test_authenticate_user_missing_credentials_HTTP_400_bad_request(self):
        """Test authenticating a user with missing credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_missing, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authenticate_user_missing_credentials_access_token_not_received(self):  # noqa E501
        """Test authenticating a user with missing credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_missing, format='json')
        self.assertNotIn('access', response.data)

    def test_authenticate_user_missing_credentials_refresh_token_not_received(self):  # noqa E501
        """Test authenticating a user with missing credentials."""
        response = self.client.post(
            URL_TOKEN_PAIR, self.data_missing, format='json')
        self.assertNotIn('refresh', response.data)
