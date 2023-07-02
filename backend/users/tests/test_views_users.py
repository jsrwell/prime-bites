from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import PrimeUser
from rest_framework.test import APIClient


class UserCreationTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('users:create')
        self.data = {
            'email': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }

    def test_create_user_success(self):
        """
        Test creating a user with valid data.
        """
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.data['email'])
        self.assertNotIn('id', response.data)

    def test_create_user_missing_email(self):
        """
        Test creating a user with missing email field.
        """
        data = self.data.copy()
        data.pop('email')

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_existing_email(self):
        """
        Test creating a user with an email that already exists.
        """
        PrimeUser.objects.create_user(**self.data)

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email']
                         [0], 'This email is already in use.')


class TokenCreationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('users:token')
        self.user = PrimeUser.objects.create_user(
            email='test@example.com',
            password='mypassword'
        )

    def test_create_token_success(self):
        """
        Test creating a token with valid credentials.
        """
        data = {
            'email': 'test@example.com',
            'password': 'mypassword',
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_create_token_invalid_credentials(self):
        """
        Test creating a token with invalid credentials.
        """
        data = {
            'email': 'test@example.com',
            'password': 'wrongpassword',
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CurrentUserTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('users:me')
        self.user = PrimeUser.objects.create_user(
            email='test@example.com',
            password='mypassword',
            first_name='John',
            last_name='Doe'
        )

    def test_get_current_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
