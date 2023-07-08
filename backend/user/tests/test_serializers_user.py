"""
Users Serializers Tests
"""
from django.test import TestCase
from user.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'email': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        self.invalid_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 123  # Invalid data type
        }

    def test_serializer_fields(self):
        """Test if the serializer contains the expected fields."""
        serializer = UserSerializer()
        expected_fields = ['email', 'password', 'first_name', 'last_name']
        self.assertEqual(set(serializer.fields.keys()), set(expected_fields))

    def test_serializer_valid_data_email(self):
        """ Test if the serializer saves valid data correctly. """
        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, self.valid_data['email'])

    def test_serializer_valid_data_first_name(self):
        """ Test if the serializer saves the first name correctly."""
        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.first_name, self.valid_data['first_name'])

    def test_serializer_valid_data_last_name(self):
        """Test if the serializer saves the last name correctly."""
        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.last_name, self.valid_data['last_name'])

    def test_serializer_invalid_data(self):
        """Test if the serializer handles invalid data correctly."""
        serializer = UserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
