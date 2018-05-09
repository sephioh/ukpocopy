import re

POSTCODE_AREA_REGEX_PATTERN = "(^[a-zA-Z]+)"
POSTCODE_DISTRICT_DIGITS_REGEX_PATTERN = "^[a-zA-Z]+(\d{1,2})"

AREAS_WITH_ONLY_SINGLE_DIGIT_DISTRICT = [
    "BR", "FY", "HA", "HD", "HG", "HR", "HS", "HX", "JE", "LD", "SM", "SR", "WC", "WN", "ZE"
]
AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICT = ["AB", "LL", "SO"]


def validate_postcode(code):
    validation_rules = [
        validate_postcode_using_regex,
        validate_single_digit_district,
        validate_double_digit_district
    ]

    for validation_rule in validation_rules:
        if not validation_rule(code):
            return False

    return True


def validate_postcode_using_regex(code):
    UK_POSTCODE_REGEX = "^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})" \
                        "|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])" \
                        "|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$"

    return True if re.match(UK_POSTCODE_REGEX, code) else False


def validate_single_digit_district(code):
    area = _retrieve_postcode_area(code)
    district_digits = _retrieve_postcode_district_digits(code)

    if area in AREAS_WITH_ONLY_SINGLE_DIGIT_DISTRICT and len(district_digits) != 1:
        return False

    return True


def validate_double_digit_district(code):
    area = _retrieve_postcode_area(code)
    district_digits = _retrieve_postcode_district_digits(code)

    if area in AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICT and len(district_digits) != 2:
        return False

    return True


def _retrieve_postcode_area(code):
    area = re.match(POSTCODE_AREA_REGEX_PATTERN, code).group(0)
    return area


def _retrieve_postcode_district_digits(code):
    district_digits = re.match(POSTCODE_DISTRICT_DIGITS_REGEX_PATTERN, code).group(1)
    return district_digits
