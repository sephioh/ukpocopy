import re

from ukpocopy.exceptions import InvalidPostalCodeException
from ukpocopy.validators import validate_uk_postal_code


class UKPostalCode(object):
    __POSTCODE_AREA_REGEX_PATTERN = "(^[a-zA-Z]+)"
    __validator = validate_uk_postal_code

    def __init__(self, postal_code):
        if not self.__validate(postal_code):
            raise InvalidPostalCodeException

        self.code = postal_code

    @classmethod
    def __validate(cls, postal_code):
        return cls.__validator(postal_code)

    @property
    def outward_code(self):
        return self.code.split(' ')[0]

    @property
    def inward_code(self):
        return self.code.split(' ')[1]

    @property
    def postcode_area(self):
        return re.match(self.__POSTCODE_AREA_REGEX_PATTERN, self.outward_code).group(0)

    @property
    def postcode_district(self):
        return self.outward_code

    @property
    def postcode_sector(self):
        return "%s %s" % (self.outward_code, self.inward_code[0])

    @property
    def postcode_unit(self):
        return self.inward_code[-2:]
