from unittest import TestCase

from ukpocopy.postcodes import UKPostcode


class TestUKPostCodeFormatter(TestCase):
    def test_format_postcode_shows_uppercase_code(self):
        postcode = UKPostcode("sw1w 0ny")
        self.assertEqual("SW1W 0NY", '{}'.format(postcode))

    def test_format_postcode_using_outward_code_and_inward_code_and_string_literals(self):
        postcode = UKPostcode("SW1W 0NY")
        self.assertEqual("SW1W 0NY", f"{postcode.outward_code} {postcode.inward_code}")

    def test_format_postcode_with_lower_case_letters(self):
        postcode = UKPostcode("SW1W 0NY")
        self.assertEqual("sw1w 0ny", f"{postcode.code.lower()}")

    def test_format_postcode_without_space(self):
        postcode = UKPostcode("SW1W 0NY")
        self.assertEqual("SW1W0NY", f"{postcode.outward_code}{postcode.inward_code}")
