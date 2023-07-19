"""
Test Model Customer
"""
from django.test import TestCase
from user.models import User, Customer


class CustomerModelTest(TestCase):
    def setUp(self):
        # Create user first
        self.expected_email = 'test@example.com'
        self.password = 'mypassword'
        self.user = User.objects.create_user(
            email=self.expected_email,
            password=self.password)

        # Make user a customer
        self.expected_cpf = '12345678901'
        self.expected_phone = '1234567890'

        # The signal should have already created the Customer instance
        self.customer = Customer.objects.get(user=self.user)

        # Update the attributes of the existing Customer instance
        self.customer.cpf = self.expected_cpf
        self.customer.phone = self.expected_phone
        self.customer.save()

    def test_customer_creation_successfully(self):
        """Test creating a customer with success."""
        self.assertEqual(self.customer.user.email, self.expected_email)

    def test_customer_creation_return_correct_cpf(self):
        """Test creating a customer return correct cpf."""
        self.assertEqual(self.customer.cpf, self.expected_cpf)

    def test_customer_creation_return_correct_phone(self):
        """Test creating a customer return correct phone."""
        self.assertEqual(self.customer.phone, self.expected_phone)
