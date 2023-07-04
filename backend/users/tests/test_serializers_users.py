"""
Users Serializers Tests
"""

from django.test import TestCase
from users.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def test_serializer_fields(self):
        """Test the serializer fields."""
        serializer = UserSerializer()
        expected_fields = ['email', 'password', 'first_name', 'last_name']

        self.assertEqual(set(serializer.fields.keys()), set(expected_fields))

    def test_serializer_valid_data(self):
        """Test serializer with valid data."""
        data = {
            'email': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])

    def test_serializer_invalid_data(self):
        """Test serializer with invalid data."""
        data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 123  # Invalid data type
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
