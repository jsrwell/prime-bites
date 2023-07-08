"""
Users Model Tests
"""
from django.test import TestCase
from user.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.email = 'test@example.com'
        self.password = 'mypassword'
        self.first_name = 'John'
        self.last_name = 'Doe'
        self.user = User.objects.create_user(
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_create_user_with_required_email(self):
        """Test creating a user with the required email field."""
        self.assertEqual(self.user.email, self.email)

    def test_create_user_with_required_password(self):
        """Test creating a user with the required password field."""
        self.assertTrue(self.user.check_password(self.password))

    def test_create_user_with_optional_first_name(self):
        """Test creating a user with the optional first name."""
        self.assertEqual(self.user.first_name, self.first_name)

    def test_create_user_with_optional_last_name(self):
        """Test creating a user with the optional last name."""
        self.assertEqual(self.user.last_name, self.last_name)

    def test_save_sets_first_name_from_email(self):
        """Test if the save() method sets the first name from the email."""
        self.user2 = User.objects.create_user(
            email="testmyemail@example.com",
            password="Test123@",
        )
        expected_first_name = "testmyemail"
        self.assertEqual(self.user2.first_name, expected_first_name)
