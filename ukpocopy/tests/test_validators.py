from unittest import TestCase

from ukpocopy.exceptions import InvalidSingleDigitDistrictValidationError, \
    InvalidDoubleDigitDistrictValidationError, InvalidZeroDigitForDistrictAreaValidationError, \
    InvalidTenDigitForDistrictAreaValidationError, InvalidFirstPositionLetterValidationError, \
    InvalidSecondPositionLetterValidationError, InvalidThirdPositionLetterValidationError, \
    InvalidFourthPositionLetterValidationError, InvalidFinalTwoLettersError, \
    InvalidPostcodeFormatValidationError
from ukpocopy.validators import validate_postcode, validate_single_digit_district, \
    validate_double_digit_district, validate_zero_district, validate_first_position_letter, \
    validate_second_position_letter, validate_third_position_letter, \
    validate_fourth_position_letter, validate_final_two_letters, validate_postcode_using_regex


class TestValidatePostcode(TestCase):
    def test_valid_postcode(self):
        self.assertTrue(validate_postcode("SW1W 0NY"))


class TestPostcodeRegexValidator(TestCase):
    def test_valid_postcode_format(self):
        self.assertIsNone(validate_postcode_using_regex("BR3 4TU"))

    def test_valid_postcode_with_AA9A_9AA_format(self):
        self.assertIsNone(validate_postcode_using_regex("EC1A 1BB"))

    def test_valid_postcode_with_A9A_9AA_format(self):
        self.assertIsNone(validate_postcode_using_regex("W1A 0AX"))

    def test_valid_postcode_with_A9_9AA_format(self):
        self.assertIsNone(validate_postcode_using_regex("M1 1AE"))

    def test_valid_postcode_with_A99_9AA_format(self):
        self.assertIsNone(validate_postcode_using_regex("B33 8TH"))

    def test_valid_postcode_with_AA9_9AA_format(self):
        self.assertIsNone(validate_postcode_using_regex("CR0 6XH"))

    def test_valid_postcode_with_AA99_9AA_format(self):
        self.assertIsNone(validate_postcode_using_regex("DN55 1PT"))

    def test_valid_postcode_with_lower_case_letters(self):
        self.assertIsNone(validate_postcode_using_regex("dn55 1pt"))

    def test_valid_postcode_with_mixed_case_letters(self):
        self.assertIsNone(validate_postcode_using_regex("dn55 1PT"))

    def test_postcode_without_space_is_invalid(self):
        with self.assertRaises(InvalidPostcodeFormatValidationError):
            validate_postcode_using_regex("BR34TU")

    def test_valid_postcode_without_space_is_invalid(self):
        with self.assertRaises(InvalidPostcodeFormatValidationError):
            validate_postcode_using_regex("SW1W0NY")

    def test_invalid_postcode_is_invalid(self):
        with self.assertRaises(InvalidPostcodeFormatValidationError):
            validate_postcode_using_regex("0000 000")

    def test_empty_postcode_is_invalid(self):
        with self.assertRaises(InvalidPostcodeFormatValidationError):
            validate_postcode_using_regex("")


class TestSingleDigitDistrictValidator(TestCase):
    def test_area_with_only_single_digit_district(self):
        self.assertIsNone(validate_single_digit_district("BR3 4TU"))

    def test_when_multiple_digit_for_single_digit_district_area_is_invalid(self):
        with self.assertRaises(InvalidSingleDigitDistrictValidationError):
            validate_single_digit_district("BR30 4TU")

    def test_no_restriction_for_non_single_digit_district_area(self):
        self.assertIsNone(validate_single_digit_district("B33 8TH"))


class TestDoubleDigitDistrictValidator(TestCase):
    def test_area_with_double_digit_district(self):
        self.assertIsNone(validate_double_digit_district("AB10 1TB"))

    def test_single_digit_district_postcode_for_double_digit_district_area_is_invalid(self):
        with self.assertRaises(InvalidDoubleDigitDistrictValidationError):
            self.assertFalse(validate_double_digit_district("AB1 1TB"))

    def test_no_restriction_for_non_double_digit_district_area(self):
        self.assertIsNone(validate_double_digit_district("BR3 4TU"))

    def test_invalid_postcode_AB1_1AA_is_invalid(self):
        with self.assertRaises(InvalidDoubleDigitDistrictValidationError):
            validate_postcode("AB1 1AA")


class TestZeroDistrictValidator(TestCase):
    def test_zero_district_area(self):
        self.assertIsNone(validate_zero_district("BL0 0AA"))

    def test_BL_area_with_10_as_district_area_digits_is_invalid(self):
        with self.assertRaises(InvalidTenDigitForDistrictAreaValidationError):
            self.assertFalse(validate_zero_district("BL10 0AA"))

    def test_BS_area_is_valid_with_0_district_area_digit(self):
        self.assertIsNone(validate_zero_district("BS0 0AA"))

    def test_BS_area_is_valid_with_10_district_area_digits(self):
        self.assertIsNone(validate_zero_district("BS10 0AA"))

    def test_zero_district_for_invalid_zero_district_area(self):
        with self.assertRaises(InvalidZeroDigitForDistrictAreaValidationError):
            self.assertFalse(validate_zero_district("AB0 0AA"))

    def test_no_restriction_for_non_zero_district_area(self):
        self.assertIsNone(validate_double_digit_district("BR3 4TU"))


class TestFirstPositionLetterValidator(TestCase):
    def test_valid_first_position_letter(self):
        self.assertIsNone(validate_first_position_letter("BL0 0AA"))

    def test_Q_is_an_invalid_first_position_letter(self):
        with self.assertRaises(InvalidFirstPositionLetterValidationError):
            self.assertFalse(validate_first_position_letter("QL0 0AA"))

    def test_V_is_an_invalid_first_position_letter(self):
        with self.assertRaises(InvalidFirstPositionLetterValidationError):
            self.assertFalse(validate_first_position_letter("VL0 0AA"))

    def test_X_is_an_invalid_first_position_letter(self):
        with self.assertRaises(InvalidFirstPositionLetterValidationError):
            self.assertFalse(validate_first_position_letter("XL0 0AA"))


class TestSecondPositionLetterValidator(TestCase):
    def test_valid_second_letter(self):
        self.assertIsNone(validate_second_position_letter("BL0 0AA"))

    def test_I_is_an_invalid_first_position_letter(self):
        with self.assertRaises(InvalidSecondPositionLetterValidationError):
            self.assertFalse(validate_second_position_letter("BI0 0AA"))

    def test_J_is_an_invalid_first_position_letter(self):
        with self.assertRaises(InvalidSecondPositionLetterValidationError):
            self.assertFalse(validate_second_position_letter("BJ0 0AA"))

    def test_Z_is_an_invalid_first_position_letter(self):
        with self.assertRaises(InvalidSecondPositionLetterValidationError):
            self.assertFalse(validate_second_position_letter("BZ0 0AA"))


class TestThirdPositionLetterValidator(TestCase):
    def test_valid_third_letter_for_A9A_format(self):
        self.assertIsNone(validate_third_position_letter("W1A 0AX"))

    def test_invalid_third_letter_for_A9A_format(self):
        with self.assertRaises(InvalidThirdPositionLetterValidationError):
            self.assertFalse(validate_third_position_letter("W1I 0AX"))


class TestFourthPositionLetterValidator(TestCase):
    def test_valid_fourth_letter_for_AA9A_format(self):
        self.assertIsNone(validate_fourth_position_letter("EC1A 1BB"))

    def test_invalid_fourth_letter_for_AA9A_format(self):
        with self.assertRaises(InvalidFourthPositionLetterValidationError):
            self.assertFalse(validate_fourth_position_letter("EC1C 1BB"))


class TestFinalTwoLettersValidator(TestCase):
    def test_valid_final_two_letters(self):
        self.assertIsNone(validate_final_two_letters("W1A 0AX"))

    def test_invalid_final_letter(self):
        with self.assertRaises(InvalidFinalTwoLettersError):
            self.assertFalse(validate_final_two_letters("W1A 0AC"))

    def test_invalid_next_to_last_letter(self):
        with self.assertRaises(InvalidFinalTwoLettersError):
            self.assertFalse(validate_final_two_letters("W1A 0CX"))
