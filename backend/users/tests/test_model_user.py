"""
Test User model
"""
from django.test import TestCase
from users.models import User
from django.utils.text import slugify


class UserModelTest(TestCase):
    def test_create_user_with_required_email(self):
        """
        Test creating a user with the required email field.
        """
        email = 'test@example.com'
        password = 'mypassword'

        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)

    def test_create_user_with_required_password(self):
        """
        Test creating a user with the required password field.
        """
        email = 'test@example.com'
        password = 'mypassword'

        user = User.objects.create_user(email=email, password=password)

        self.assertTrue(user.check_password(password))

    def test_create_user_with_optional_first_name(self):
        """
        Test creating a user with the optional first name.
        """
        email = 'test@example.com'
        password = 'mypassword'
        first_name = 'John'

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
        )

        self.assertEqual(user.first_name, first_name)

    def test_create_user_with_optional_last_name(self):
        """
        Test creating a user with the optional last name.
        """
        email = 'test@example.com'
        password = 'mypassword'
        last_name = 'Doe'

        user = User.objects.create_user(
            email=email,
            password=password,
            last_name=last_name
        )

        self.assertEqual(user.last_name, last_name)

    def test_save_sets_first_name_from_email(self):
        """
        Test if the save() method sets the first name from the email.
        """
        self.user = User(email='test@example.com')
        self.user.save()

        expected_first_name = slugify('test').split('-')[0]
        self.assertEqual(self.user.first_name, expected_first_name)

    def test_get_first_name_from_email(self):
        """
        Test if the get_first_name_from_email() method
        returns the correct first name from the email.
        """
        self.user = User(email='test@example.com')
        first_name = self.user.get_first_name_from_email()

        expected_first_name = slugify('test').split('-')[0]
        self.assertEqual(first_name, expected_first_name)
