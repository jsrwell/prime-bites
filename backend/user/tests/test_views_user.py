"""
Teste User Views
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User
from core.utils import get_first_name_from_email


CREATE_URL = reverse('user:create')


class UserCreationTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'email': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }

    def test_create_user_success_HTTP_201(self):
        """Test creating a user with valid data."""
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_success_prime_bites_message(self):
        """Test creating a user with valid data."""
        expected = f'User {self.data["first_name"]} has been created!'
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.data['prime_bites_message'], expected)

    def test_create_user_success_email(self):
        """Test if the created user has the correct email."""
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.data['email'], self.data['email'])

    def test_create_user_fail_missing_email(self):
        """Test creating a user with missing email field."""
        self.data.pop('email')
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_fail_missing_last_name(self):
        """Test creating a user with missing last_name field."""
        self.data.pop('last_name')
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['last_name'], '')

    def test_create_user_fail_existing_email(self):
        """ Test creating a user with an email that already exists."""
        User.objects.create_user(**self.data)
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['email'][0], 'This email is already in use.'
        )

    def test_create_user_auto_fill_first_name_from_email(self):
        """Test if the first name is automatically filled from the email."""
        self.data.pop('first_name')
        expected_first_name = get_first_name_from_email(self.data['email'])
        response = self.client.post(CREATE_URL, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], expected_first_name)
