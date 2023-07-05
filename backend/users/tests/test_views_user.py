"""
Teste User Views
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from django.utils.text import slugify

CREATE_URL = reverse('user:create')


class UserCreationTestCase(APITestCase):
    def setUp(self):
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
        response = self.client.post(CREATE_URL, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_success_email(self):
        """
        Test if the created user has the correct email.
        """
        response = self.client.post(CREATE_URL, self.data, format='json')

        self.assertEqual(response.data['email'], self.data['email'])

    def test_create_user_fail_missing_email(self):
        """
        Test creating a user with missing email field.
        """
        data = self.data.copy()
        data.pop('email')

        response = self.client.post(CREATE_URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_fail_existing_email(self):
        """
        Test creating a user with an email that already exists.
        """
        User.objects.create_user(**self.data)

        response = self.client.post(CREATE_URL, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['email'][0], 'This email is already in use.'
        )

    def test_create_user_auto_fill_first_name_from_email(self):
        """
        Test if the first name is automatically filled from the email.
        """
        data = self.data.copy()
        data.pop('first_name')

        response = self.client.post(CREATE_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email=self.data['email'])
        expected_first_name = slugify(
            self.data['email'].split('@')[0]).split('-')[0]

        self.assertEqual(user.first_name, expected_first_name)
