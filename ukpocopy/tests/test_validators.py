from unittest import TestCase

from ukpocopy.validators import validate_postcode, validate_single_digit_district, \
    validate_double_digit_district, validate_zero_district, validate_first_position_letter, \
    validate_second_position_letter, validate_third_position_letter, validate_fourth_position_letter

VALID_POSTCODE = "SW1W 0NY"
VALID_POSTCODE_WITH_AA9A_9AA_FORMAT = "EC1A 1BB"
VALID_POSTCODE_WITH_A9A_9AA_FORMAT = "W1A 0AX"
VALID_POSTCODE_WITH_A9_9AA_FORMAT = "M1 1AE"
VALID_POSTCODE_WITH_A99_9AA_FORMAT = "B33 8TH"
VALID_POSTCODE_WITH_AA9_9AA_FORMAT = "CR0 6XH"
VALID_POSTCODE_WITH_AA99_9AA_FORMAT = "DN55 1PT"
VALID_POSTCODE_WITH_LOWER_CASE_LETTERS = "dn55 1pt"
VALID_POSTCODE_WITH_MIXED_CASE_LETTERS = "dn55 1PT"

INVALID_POSTCODE = "0000 000"
INVALID_POSTCODE_AB1_1AA = "AB1 1AA"
VALID_POSTCODE_WITHOUT_SPACE = "SW1W0NY"
EMPTY_POSTCODE = ""


class TestValidatePostcode(TestCase):
    def test_valid_postcode_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE))

    def test_valid_postcode_with_AA9A_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_AA9A_9AA_FORMAT))

    def test_valid_postcode_with_A9A_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_A9A_9AA_FORMAT))

    def test_valid_postcode_with_A9_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_A9_9AA_FORMAT))

    def test_valid_postcode_with_A99_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_A99_9AA_FORMAT))

    def test_valid_postcode_with_AA9_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_AA9_9AA_FORMAT))

    def test_valid_postcode_with_AA99_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_AA99_9AA_FORMAT))

    def test_valid_postcode_with_lower_case_letters_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_LOWER_CASE_LETTERS))

    def test_valid_postcode_with_mixed_case_letters_returns_true(self):
        self.assertTrue(validate_postcode(VALID_POSTCODE_WITH_MIXED_CASE_LETTERS))

    def test_valid_postcode_without_space_returns_false(self):
        self.assertFalse(validate_postcode(VALID_POSTCODE_WITHOUT_SPACE))

    def test_invalid_postcode_returns_false(self):
        self.assertFalse(validate_postcode(INVALID_POSTCODE))

    def test_invalid_postcode_AB1_1AA_returns_false(self):
        self.assertFalse(validate_postcode(INVALID_POSTCODE_AB1_1AA))

    def test_empty_postcode_returns_false(self):
        self.assertFalse(validate_postcode(EMPTY_POSTCODE))


class TestSingleDigitDistrictValidator(TestCase):
    def test_area_with_only_single_digit_district(self):
        self.assertTrue(validate_single_digit_district("BR3 4TU"))

    def test_multiple_digit_district_postcode_for_single_digit_district_area_returns_false(self):
        self.assertFalse(validate_single_digit_district("BR30 4TU"))

    def test_no_restriction_for_non_single_digit_district_area(self):
        self.assertTrue(validate_single_digit_district("B33 8TH"))


class TestDoubleDigitDistrictValidator(TestCase):
    def test_area_with_double_digit_district(self):
        self.assertTrue(validate_double_digit_district("AB10 1TB"))

    def test_single_digit_district_postcode_for_double_digit_district_area_returns_false(self):
        self.assertFalse(validate_double_digit_district("AB1 1TB"))

    def test_no_restriction_for_non_double_digit_district_area(self):
        self.assertTrue(validate_double_digit_district("BR3 4TU"))


class TestZeroDistrictValidator(TestCase):
    def test_zero_district_area(self):
        self.assertTrue(validate_zero_district("BL0 0AA"))

    def test_BS_area_is_valid_with_10_district_area_digits(self):
        self.assertTrue(validate_zero_district("BS10 0AA"))

    def test_BS_area_is_invalid_with_other_district_area_digits(self):
        self.assertFalse(validate_zero_district("BS9 0AA"))

    def test_non_zero_district_for_zero_district_area_returns_false(self):
        self.assertFalse(validate_zero_district("BL1 0AA"))

    def test_no_restriction_for_non_zero_district_area(self):
        self.assertTrue(validate_double_digit_district("BR3 4TU"))


class TestFirstPositionLetterValidator(TestCase):
    def test_valid_first_position_letter(self):
        self.assertTrue(validate_first_position_letter("BL0 0AA"))

    def test_Q_is_an_invalid_first_position_letter(self):
        self.assertFalse(validate_first_position_letter("QL0 0AA"))

    def test_V_is_an_invalid_first_position_letter(self):
        self.assertFalse(validate_first_position_letter("VL0 0AA"))

    def test_X_is_an_invalid_first_position_letter(self):
        self.assertFalse(validate_first_position_letter("XL0 0AA"))


class TestSecondPositionLetterValidator(TestCase):
    def test_valid_second_letter(self):
        self.assertTrue(validate_second_position_letter("BL0 0AA"))

    def test_I_is_an_invalid_first_position_letter(self):
        self.assertFalse(validate_second_position_letter("BI0 0AA"))

    def test_J_is_an_invalid_first_position_letter(self):
        self.assertFalse(validate_second_position_letter("BJ0 0AA"))

    def test_Z_is_an_invalid_first_position_letter(self):
        self.assertFalse(validate_second_position_letter("BZ0 0AA"))


class TestThirdPositionLetterValidator(TestCase):
    def test_valid_third_letter_for_A9A_format(self):
        self.assertTrue(validate_third_position_letter("W1A 0AX"))

    def test_invalid_third_letter_for_A9A_format(self):
        self.assertFalse(validate_third_position_letter("W1I 0AX"))


class TestFourthPositionLetterValidator(TestCase):
    def test_valid_fourth_letter_for_AA9A_format(self):
        self.assertTrue(validate_fourth_position_letter("EC1A 1BB"))

    def test_invalid_fourth_letter_for_AA9A_format(self):
        self.assertFalse(validate_fourth_position_letter("EC1C 1BB"))
