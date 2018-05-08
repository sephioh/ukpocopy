from unittest import TestCase

from ukpocopy.validators import validate_uk_postcode

VALID_UK_POSTCODE = "SW1W 0NY"
INVALID_UK_POSTCODE = "0000 000"
EMPTY_UK_POSTCODE = ""


class TestValidateUkPostcode(TestCase):
    def test_validates_a_valid_postcode_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_UK_POSTCODE))

    def test_validates_a_invalid_postcode_returns_false(self):
        self.assertFalse(validate_uk_postcode(INVALID_UK_POSTCODE))

    def test_empty_postcode_returns_false(self):
        self.assertFalse(validate_uk_postcode(EMPTY_UK_POSTCODE))
