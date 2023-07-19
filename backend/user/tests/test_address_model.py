"""
Teste Address Model
"""
from django.test import TestCase
from user.models import User, Customer, Address


class AddressModelTest(TestCase):
    def setUp(self):
        # Create a User first
        self.email = 'test@example.com'
        self.password = 'mypassword'
        self.user = User.objects.create_user(
            email=self.email,
            password=self.password
        )

        # Create a Customer
        self.expected_cpf = '12345678901'
        self.expected_phone = '1234567890'

        # The signal should have already created the Customer instance
        self.customer = Customer.objects.get(user=self.user)

        # Update the attributes of the existing Customer instance
        self.customer.cpf = self.expected_cpf
        self.customer.phone = self.expected_phone
        self.customer.save()

        # Create an Address
        self.street = 'Test Street'
        self.number = '123'
        self.neighborhood = 'Test Neighborhood'
        self.complement = 'Test Complement'
        self.city = 'Test City'
        self.state = 'Test State'
        self.country = 'Test Country'
        self.zip_code = '12345'
        self.address = Address.objects.create(
            customer=self.customer,
            street=self.street,
            number=self.number,
            neighborhood=self.neighborhood,
            complement=self.complement,
            city=self.city,
            state=self.state,
            country=self.country,
            zip_code=self.zip_code
        )

    def test_address_creation_return_correct_customer(self):
        """Test creating an address returns the correct customer."""
        self.assertEqual(self.address.customer, self.customer)

    def test_address_creation_return_correct_street(self):
        """Test creating an address returns the correct street."""
        self.assertEqual(self.address.street, self.street)

    def test_address_creation_return_correct_number(self):
        """Test creating an address returns the correct number."""
        self.assertEqual(self.address.number, self.number)

    def test_address_creation_return_correct_neighborhood(self):
        """Test creating an address returns the correct neighborhood."""
        self.assertEqual(self.address.neighborhood, self.neighborhood)

    def test_address_creation_return_correct_complement(self):
        """Test creating an address returns the correct complement."""
        self.assertEqual(self.address.complement, self.complement)

    def test_address_creation_return_correct_city(self):
        """Test creating an address returns the correct city."""
        self.assertEqual(self.address.city, self.city)

    def test_address_creation_return_correct_state(self):
        """Test creating an address returns the correct state."""
        self.assertEqual(self.address.state, self.state)

    def test_address_creation_return_correct_country(self):
        """Test creating an address returns the correct country."""
        self.assertEqual(self.address.country, self.country)

    def test_address_creation_return_correct_zip_code(self):
        """Test creating an address returns the correct zip code."""
        self.assertEqual(self.address.zip_code, self.zip_code)
