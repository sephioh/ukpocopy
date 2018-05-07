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
        postal_code = UKPostalCode("SW1W 0NY")
        self.assertEqual("SW1W", postal_code.outward_code)

    def test_retrieve_inward_code(self):
        postal_code = UKPostalCode("SW1W 0NY")
        self.assertEqual("0NY", postal_code.inward_code)

    def test_retrieve_postcode_area_with_two_chars(self):
        postal_code = UKPostalCode("SW1W 0NY")
        self.assertEqual("SW", postal_code.postcode_area)

    def test_retrieve_postcode_area_with_single_char(self):
        postal_code = UKPostalCode("L1 8JQ")
        self.assertEqual("L", postal_code.postcode_area)
