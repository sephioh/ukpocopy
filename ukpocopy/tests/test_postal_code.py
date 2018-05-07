from unittest import TestCase

from ukpocopy.postal_code import UKPostalCode

VALID_UK_POSTAL_CODE = "SW1W 0NY"
INVALID_UK_POSTAL_CODE = "0000 000"
EMPTY_UK_POSTAL_CODE = ""


class TestUKPostalCodeValidation(TestCase):
    def test_valid_postal_code_returns_true(self):
        postal_code = UKPostalCode(VALID_UK_POSTAL_CODE)
        self.assertTrue(postal_code.is_valid())

    def test_invalid_postal_code_returns_false(self):
        postal_code = UKPostalCode(INVALID_UK_POSTAL_CODE)
        self.assertFalse(postal_code.is_valid())

    def test_empty_postal_code_returns_false(self):
        postal_code = UKPostalCode(EMPTY_UK_POSTAL_CODE)
        self.assertFalse(postal_code.is_valid())
