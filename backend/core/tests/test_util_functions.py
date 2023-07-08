from django.test import SimpleTestCase
from core.utils import get_first_name_from_email


class TestUtilFunctions(SimpleTestCase):
    """Test if the utils functions is working."""

    def test_get_first_name_from_email(self):
        """Test get_first_name_from_email() method."""
        test_email = "testmyemail@example.com"
        expected_first_name = "testmyemail"
        first_name = get_first_name_from_email(test_email)
        self.assertEqual(first_name, expected_first_name)
