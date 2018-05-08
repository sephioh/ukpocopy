# ukpocopy
[![PyPI version](https://badge.fury.io/py/ukpocopy.svg)](https://badge.fury.io/py/ukpocopy)
[![Codeship Status for sephioh/ukpocopy](https://app.codeship.com/projects/565cad70-3455-0136-6a61-7a9459f2f135/status?branch=master)](https://app.codeship.com/projects/289061)
[![codecov](https://codecov.io/gh/sephioh/ukpocopy/branch/master/graph/badge.svg)](https://codecov.io/gh/sephioh/ukpocopy)

A python package for UK Postcodes validation and formatting.

# Installation

Install using `pip`:

```
pip install -U ukpocopy
```

# How to use

## Validation
To validate a postcode, you can use `validate_postcode` function directly:
```
from ukpocopy.validators validate_postcode


validate_postcode("SW1W 0NY")  # returns True
validate_postcode("0000 000")  # returns False
```

Postcode validations also happens during `UKPostcode` instantiation:
```
from ukpocopy.postcodes import UKPostcode


postcode = UKPostcode("SW1W 0NY")  # returns UKPostcode instance
postcode = UKPostcode("0000 000")  # raises InvalidPostcodeException
```

## Formatting
`ukpocopy` uses [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals) to format postcodes.
`UKPostcode` has the following attributes you want to use in order to render them the way you need:
* [outward_code](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Outward_code)
* [inward_code](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Inward_code)
* [postcode_area](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_area)
* [postcode_district](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_district)
* [postcode_sector](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_sector)
* [postcode_unit](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Postcode_unit)

### Examples
#### Display postcode without space
```
postcode = UKPostcode("SW1W 0NY")
f"{postcode.outward_code}{postcode.inward_code}"  # returns "SW1W0NY"
```

#### Display postcode with lower case letters
```
postcode = UKPostcode("SW1W 0NY")
f"{postcode.code.lower()}"  # returns "sw1w 0ny"
```

# Testing
Run tests using this command:
```
make test
```

# Versioning
This projects uses [Semantic Versioning](https://semver.org/) and [bumpversion](https://github.com/peritus/bumpversion). Use one the following commands to appropriately update `ukpocopy` version:
* ```make bump_patch_version```
* ```make bump_minor_version```
* ```make bump_major_version```

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
