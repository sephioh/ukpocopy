from unittest import TestCase

from ukpocopy.validators import validate_uk_postal_code

VALID_UK_POSTAL_CODE = "SW1W 0NY"
INVALID_UK_POSTAL_CODE = "0000 000"
EMPTY_UK_POSTAL_CODE = ""


class TestValidateUkPostalCode(TestCase):
    def test_validates_a_valid_postal_code_returns_true(self):
        self.assertTrue(validate_uk_postal_code(VALID_UK_POSTAL_CODE))

    def test_validates_a_invalid_postal_code_returns_false(self):
        self.assertFalse(validate_uk_postal_code(INVALID_UK_POSTAL_CODE))

    def test_empty_postal_code_returns_false(self):
        self.assertFalse(validate_uk_postal_code(EMPTY_UK_POSTAL_CODE))
