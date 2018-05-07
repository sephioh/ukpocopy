from unittest import TestCase

from ukpocopy.postal_codes import UKPostalCode
from ukpocopy.exceptions import InvalidPostalCodeException

VALID_UK_POSTAL_CODE = "SW1W 0NY"
INVALID_UK_POSTAL_CODE = "0000 000"


class TestUKPostalCode(TestCase):
    def test_instantiate_valid_postal_code(self):
        postal_code = UKPostalCode(VALID_UK_POSTAL_CODE)
        self.assertEqual(VALID_UK_POSTAL_CODE, postal_code.code)

    def test_instantiate_invalid_postal_code_raises_exception(self):
        with self.assertRaises(InvalidPostalCodeException):
            UKPostalCode(INVALID_UK_POSTAL_CODE)

    def test_retrieve_outward_code(self):
        with self.assertRaises(InvalidPostalCodeException):
            UKPostalCode(INVALID_UK_POSTAL_CODE)
