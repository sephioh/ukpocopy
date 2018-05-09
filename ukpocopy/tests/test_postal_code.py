from unittest import TestCase

from ukpocopy.exceptions import PostcodeValidationError
from ukpocopy.postcodes import UKPostcode

VALID_POSTCODE = "SW1W 0NY"
INVALID_POSTCODE = "0000 000"


class TestUKPostcode(TestCase):
    def test_instantiate_valid_postcode(self):
        postcode = UKPostcode(VALID_POSTCODE)
        self.assertEqual(VALID_POSTCODE, postcode.code)

    def test_instantiate_invalid_postcode_raises_exception(self):
        with self.assertRaises(PostcodeValidationError):
            UKPostcode(INVALID_POSTCODE)

    def test_retrieve_outward_code(self):
        postcode = UKPostcode("SW1W 0NY")
        self.assertEqual("SW1W", postcode.outward_code)

    def test_retrieve_inward_code(self):
        postcode = UKPostcode("SW1W 0NY")
        self.assertEqual("0NY", postcode.inward_code)

    def test_retrieve_postcode_area_with_two_chars(self):
        postcode = UKPostcode("SW1W 0NY")
        self.assertEqual("SW", postcode.postcode_area)

    def test_retrieve_postcode_area_with_single_char(self):
        postcode = UKPostcode("L1 8JQ")
        self.assertEqual("L", postcode.postcode_area)

    def test_retrieve_postcode_district(self):
        postcode = UKPostcode("L1 8JQ")
        self.assertEqual("L1", postcode.postcode_district)

    def test_retrieve_postcode_sector(self):
        postcode = UKPostcode("L1 8JQ")
        self.assertEqual("L1 8", postcode.postcode_sector)

    def test_retrieve_postcode_unit(self):
        postcode = UKPostcode("L1 8JQ")
        self.assertEqual("JQ", postcode.postcode_unit)
