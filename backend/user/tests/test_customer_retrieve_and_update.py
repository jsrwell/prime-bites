"""
Test Customer Retrieve and Update
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import Customer

User = get_user_model()


class UserPrimusMixin:
    """Mixin for User Creation"""

    def make_user(self,
                  email='test@example.com',
                  password='mypassword'):
        return User.objects.create_user(email=email, password=password)

    def update_user_customer(self,
                             email='test@example.com',
                             cpf="11122233344",
                             phone="(41)98765-4321"):
        customer = Customer.objects.get(email=email)
        customer.cpf = cpf
        customer.phone = phone
        customer.save()
        return customer

    def get_token(self, email='test@example.com', password='mypassword'):
        userdata = {
            'email': email,
            'password': password,
        }
        user = self.make_author(
            email=userdata.get('email'),
            password=userdata.get('password')
        )
        response = self.client.post(
            reverse('user:token_obtain_pair'), data={**userdata}
        )
        return {
            'access_token': response.data.get('access'),
            'refresh_token': response.data.get('refresh'),
            'user': user,
        }


class CustomerRetrieveUpdateViewTest(TestCase, UserPrimusMixin):
    """Customer Retrieve and Update Tests"""

    def setUp(self):
        self.email = 'test@example.com'
        self.password = 'mypassword'
        self.user = User.objects.create_user(
            email=self.email,
            password=self.password
        )
        # Make user a customer
        self.expected_cpf = '12345678901'
        self.expected_phone = '1234567890'

        # The signal should have already created the Customer instance
        self.customer = Customer.objects.get(user=self.user)

        # Update the attributes of the existing Customer instance
        self.customer.cpf = self.expected_cpf
        self.customer.phone = self.expected_phone
        self.customer.save()

        self.client = APIClient()

        # URL da view CustomerRetrieveUpdateView
        self.customer_details_url = reverse(
            'details', kwargs={'pk': self.customer.pk})

    def test_retrieve_customer_details_authenticated(self):
        """Test retrieving customer details by an authenticated user."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.customer_details_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cpf'], '12345678901')
        self.assertEqual(response.data['phone'], '1234567890')

    def test_retrieve_customer_details_unauthenticated(self):
        """Test retrieving customer details by an unauthenticated user."""
        response = self.client.get(self.customer_details_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_customer_details_authenticated(self):
        """Test updating customer details by an authenticated user."""
        self.client.force_authenticate(user=self.user)
        data = {
            'cpf': '98765432109',
            'phone': '9876543210',
        }
        response = self.client.patch(self.customer_details_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the customer instance from the database to get updated data
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.cpf, '98765432109')
        self.assertEqual(self.customer.phone, '9876543210')

    def test_update_customer_details_unauthenticated(self):
        """Test updating customer details by an unauthenticated user."""
        data = {
            'cpf': '98765432109',
            'phone': '9876543210',
        }
        response = self.client.patch(self.customer_details_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
