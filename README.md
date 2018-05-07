# ukpocopy

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

# Testing
Run tests using this command:
```
make test
```
