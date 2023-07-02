from django.test import TestCase
from users.models import PrimeUser


class UserModelTest(TestCase):
    def test_create_user_with_required_fields(self):
        """Test creating a user with required fields (email and password)."""
        email = 'test@example.com'
        password = 'mypassword'

        user = PrimeUser.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_optional_fields(self):
        """Test creating a user with optional fields (email, password, first name, and last name)."""
        email = 'test@example.com'
        password = 'mypassword'
        first_name = 'John'
        last_name = 'Doe'

        user = PrimeUser.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
