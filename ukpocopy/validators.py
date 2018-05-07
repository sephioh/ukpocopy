import re


def validate_uk_postal_code(postal_code):
    UK_POSTAL_CODE_REGEX = "^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})" \
                             "|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])" \
                             "|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$"

    return True if re.match(UK_POSTAL_CODE_REGEX, postal_code) else False
