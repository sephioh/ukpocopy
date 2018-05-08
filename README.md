# ukpocopy
[![PyPI version](https://badge.fury.io/py/ukpocopy.svg)](https://badge.fury.io/py/ukpocopy)
[![Codeship Status for sephioh/ukpocopy](https://app.codeship.com/projects/565cad70-3455-0136-6a61-7a9459f2f135/status?branch=master)](https://app.codeship.com/projects/289061)
[![codecov](https://codecov.io/gh/sephioh/ukpocopy/branch/master/graph/badge.svg)](https://codecov.io/gh/sephioh/ukpocopy)

A python package for UK Postal Code validation and formatting.

# Installation

Install using `pip`:

```
pip install -U ukpocopy
```

# How to use

## Validation
You can use validators functions directly:
```
import validate_uk_postal_code from ukpocopy.validators


validate_uk_postal_code("SW1W 0NY")  # returns True
validate_uk_postal_code("0000 000")  # returns False
```

UK postal code validations also happens during `UKPostalCode` instantiation, like this:
```
from ukpocopy.postal_codes import UKPostalCode


postal_code = UKPostalCode("SW1W 0NY")  # returns UKPostalCode instance
postal_code = UKPostalCode("0000 000")  # raises InvalidPostalCodeException
```

## Formatting
`UKPostalCode` has the following attributes you want to use in order to format UK postal codes:
* [outward_code](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Outward_code)
* [inward_code](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Inward_code)
* [postcode_area](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_area)
* [postcode_district](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_district)
* [postcode_sector](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_sector)
* [postcode_unit](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_unit)

# Testing
Run tests using this command:
```
make test
```
