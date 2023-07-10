"""
Test Model Customer
"""
from django.test import TestCase
from user.models import User, Customer


class CustomerModelTest(TestCase):
    def setUp(self):
        # Create user first
        self.email = 'test@example.com'
        self.password = 'mypassword'
        self.user = User.objects.create_user(
            email=self.email,
            password=self.password)

        # Make user a customer
        self.cpf = '12345678901'
        self.phone = '1234567890'
        self.customer = Customer.objects.create(
            user=self.user,
            cpf=self.cpf,
            phone=self.phone
        )

    def test_customer_creation_successfully(self):
        """Test creating a customer with success."""
        self.assertEqual(self.customer.user.email, self.email)

    def test_customer_creation_return_correct_cpf(self):
        """Test creating a customer return correct cpf."""
        self.assertEqual(self.customer.cpf, self.cpf)

    def test_customer_creation_return_correct_phone(self):
        """Test creating a customer return correct phone."""
        self.assertEqual(self.customer.phone, self.phone)
