import re

from ukpocopy.exceptions import InvalidPostcodeException
from ukpocopy.validators import validate_postcode


class UKPostcode(object):
    __POSTCODE_AREA_REGEX_PATTERN = "(^[a-zA-Z]+)"
    __validator = validate_postcode

    def __init__(self, postcode):
        if not self.__validate(postcode):
            raise InvalidPostcodeException

        self.code = postcode.upper()

    @classmethod
    def __validate(cls, postcode):
        return cls.__validator(postcode)

    def __str__(self):
        return self.code

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
