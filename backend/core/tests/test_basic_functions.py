# myapp/tests/test_models.py
from django.test import SimpleTestCase


class BasicFunctions(SimpleTestCase):
    """Test if the basic functions is working."""

    def test_something(self):
        """Test basic sum."""
        a = 1
        b = 1
        self.assertEqual(a+b, 2)
