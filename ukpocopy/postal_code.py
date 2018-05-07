import re


class UKPostalCode(object):
    __UK_POSTAL_CODE_REGEX = "^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$"

    def __init__(self, postal_code):
        self.postal_code = postal_code

    def is_valid(self):
        return True if re.match(self.__UK_POSTAL_CODE_REGEX, self.postal_code) else False
