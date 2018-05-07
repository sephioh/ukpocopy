from ukpocopy.exceptions import InvalidPostalCodeException
from ukpocopy.validators import validate_uk_postal_code


class UKPostalCode(object):
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
