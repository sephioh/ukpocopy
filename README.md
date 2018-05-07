# ukpocopy

A python package for UK Postal Code validation and formatting.

# Installation

Install using `pip`:

```
pip install -U ukpocopy
```


# How to use

## Validation

You can validate UK postal codes using an instance of `UKPostalCode`, like this:
```
import UKPostalCode from ukpocopy


postal_code = UKPostalCode("SW1W 0NY") # valid
postal_code.is_valid() # returns True

postal_code = UKPostalCode("0000 000") # invalid
postal_code.is_valid() # returns False
```

# Testing
Run tests using this command:
```
make test
```
