"""
Teste Model Permission
"""
from django.test import TestCase
from user.models import Permission


class PermissionModelTest(TestCase):
    def setUp(self):
        self.permission_name = 'Test Permission'
        self.permission_description = 'Test Permission Description'
        self.permission = Permission.objects.create(
            name=self.permission_name,
            description=self.permission_description
        )

    def test_permission_creation_return_correct_name(self):
        """Test creating a permission return correct name."""
        self.assertEqual(self.permission.name, self.permission_name)

    def test_permission_creation_return_correct_description(self):
        """Test creating a permission return correct description."""
        self.assertEqual(self.permission.description,
                         self.permission_description)
