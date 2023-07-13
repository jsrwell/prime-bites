"""
Teste Model Eployee
"""
from django.test import TestCase
from user.models import Permission, User, Employee


class EmployeeModelTest(TestCase):
    def setUp(self):
        # First Create a User
        self.email = 'test@example.com'
        self.password = 'mypassword'
        self.user = User.objects.create_employee(
            email=self.email,
            password=self.password)

        # Then Create Two Permission Test Permission
        self.permission_1 = Permission.objects.create(
            name='Test Permission',
            description='Test Permission Description'
        )
        self.permission_2 = Permission.objects.create(
            name='Automate Test',
            description='Test Permission Description 2'
        )

        # Finally create the Employee
        self.department = 'Test Department'
        self.employee = Employee.objects.create(
            user=self.user,
            department=self.department
        )
        self.employee.permissions.add(self.permission_1)

    def test_employee_creation_return_correct_email(self):
        """Test creating an employee return correct email."""
        self.assertEqual(self.employee.user.email, self.email)

    def test_employee_creation_return_correct_departament(self):
        """Test creating an employee return correct departament."""
        self.assertEqual(self.employee.department, self.department)

    def test_employee_creation_return_correct_permission(self):
        """Test creating an employee return correct permissions."""
        self.assertIn(self.permission_1, self.employee.permissions.all())

    def test_employee_creation_not_return_permission_not_added(self):
        """Test creating an employee return only permissions added."""
        self.assertNotIn(self.permission_2, self.employee.permissions.all())
