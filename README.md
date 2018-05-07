# ukpocopy
[ ![Codeship Status for sephioh/ukpocopy](https://app.codeship.com/projects/565cad70-3455-0136-6a61-7a9459f2f135/status?branch=master)](https://app.codeship.com/projects/289061)

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
import UKPostalCode from ukpocopy


postal_code = UKPostalCode("SW1W 0NY")  # returns UKPostalCode instance
postal_code = UKPostalCode("0000 000")  # raises InvalidPostalCodeException
```

## Formatting
`UKPostalCode` has the following attributes you want to use in order to format UK postal codes:
* outward_code
* inward_code
* postcode_area
* postcode_district
* postcode_sector
* postcode_unit

# Testing
Run tests using this command:
```
make test
```
