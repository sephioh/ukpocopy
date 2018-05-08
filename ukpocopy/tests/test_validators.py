from unittest import TestCase

from ukpocopy.validators import validate_uk_postcode

VALID_POSTCODE = "SW1W 0NY"
VALID_POSTCODE_WITH_AA9A_9AA_FORMAT = "EC1A 1BB"
VALID_POSTCODE_WITH_A9A_9AA_FORMAT = "W1A 0AX"
VALID_POSTCODE_WITH_A9_9AA_FORMAT = "M1 1AE"
VALID_POSTCODE_WITH_A99_9AA_FORMAT = "B33 8TH"
VALID_POSTCODE_WITH_AA9_9AA_FORMAT = "CR2 6XH"
VALID_POSTCODE_WITH_AA99_9AA_FORMAT = "DN55 1PT"

INVALID_POSTCODE = "0000 000"
VALID_POSTCODE_WITHOUT_SPACE = "SW1W0NY"
EMPTY_POSTCODE = ""


class TestValidateUkPostcode(TestCase):
    def test_valid_postcode_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE))

    def test_valid_postcode_with_AA9A_9AA_format_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE_WITH_AA9A_9AA_FORMAT))

    def test_valid_postcode_with_A9A_9AA_format_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE_WITH_A9A_9AA_FORMAT))

    def test_valid_postcode_with_A9_9AA_format_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE_WITH_A9_9AA_FORMAT))

    def test_valid_postcode_with_A99_9AA_format_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE_WITH_A99_9AA_FORMAT))

    def test_valid_postcode_with_AA9_9AA_format_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE_WITH_AA9_9AA_FORMAT))

    def test_valid_postcode_with_AA99_9AA_format_returns_true(self):
        self.assertTrue(validate_uk_postcode(VALID_POSTCODE_WITH_AA99_9AA_FORMAT))

    def test_valid_postcode_without_space_returns_false(self):
        self.assertFalse(validate_uk_postcode(VALID_POSTCODE_WITHOUT_SPACE))

    def test_invalid_postcode_returns_false(self):
        self.assertFalse(validate_uk_postcode(INVALID_POSTCODE))

    def test_empty_postcode_returns_false(self):
        self.assertFalse(validate_uk_postcode(EMPTY_POSTCODE))
