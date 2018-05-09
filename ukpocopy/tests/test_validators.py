from unittest import TestCase

from ukpocopy.validators import validate_postcode, validate_single_digit_district, \
    validate_double_digit_district, validate_zero_district, validate_first_position_letter, \
    validate_second_position_letter, validate_third_position_letter, \
    validate_fourth_position_letter, validate_final_two_letters

class TestValidatePostcode(TestCase):
    def test_valid_postcode_returns_true(self):
        self.assertTrue(validate_postcode("SW1W 0NY"))

    def test_valid_postcode_with_AA9A_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode("EC1A 1BB"))

    def test_valid_postcode_with_A9A_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode("W1A 0AX"))

    def test_valid_postcode_with_A9_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode("M1 1AE"))

    def test_valid_postcode_with_A99_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode("B33 8TH"))

    def test_valid_postcode_with_AA9_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode("CR0 6XH"))

    def test_valid_postcode_with_AA99_9AA_format_returns_true(self):
        self.assertTrue(validate_postcode("DN55 1PT"))

    def test_valid_postcode_with_lower_case_letters_returns_true(self):
        self.assertTrue(validate_postcode("dn55 1pt"))

    def test_valid_postcode_with_mixed_case_letters_returns_true(self):
        self.assertTrue(validate_postcode("dn55 1PT"))

    def test_valid_postcode_without_space_returns_false(self):
        self.assertFalse(validate_postcode("SW1W0NY"))

    def test_invalid_postcode_returns_false(self):
        self.assertFalse(validate_postcode("0000 000"))

    def test_invalid_postcode_AB1_1AA_returns_false(self):
        self.assertFalse(validate_postcode("AB1 1AA"))

    def test_empty_postcode_returns_false(self):
        self.assertFalse(validate_postcode(""))


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

    def test_BL_area_cannot_have_10_as_district_area_digits(self):
        self.assertFalse(validate_zero_district("BL10 0AA"))

    def test_BS_area_is_valid_with_0_district_area_digit(self):
        self.assertTrue(validate_zero_district("BS0 0AA"))

    def test_BS_area_is_valid_with_10_district_area_digits(self):
        self.assertTrue(validate_zero_district("BS10 0AA"))

    def test_zero_district_for_invalid_zero_district_area_returns_false(self):
        self.assertFalse(validate_zero_district("AB0 0AA"))

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


class TestFinalTwoLettersValidator(TestCase):
    def test_valid_final_two_letters(self):
        self.assertTrue(validate_final_two_letters("W1A 0AX"))

    def test_invalid_final_letter(self):
        self.assertFalse(validate_final_two_letters("W1A 0AC"))

    def test_invalid_next_to_last_letter(self):
        self.assertFalse(validate_final_two_letters("W1A 0CX"))
