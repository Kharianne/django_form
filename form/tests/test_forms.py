from django.test import TestCase
from ..validators import validate_ico
from django.core.exceptions import ValidationError


# I could use some parametrization, but in this case is more
# clear what is exactly tested


class TestICOValidation(TestCase):
    def test_invalid_int_ico(self):
        self.assertRaises(ValidationError, validate_ico, 1236)

    def test_invalid_string_ico(self):
        self.assertRaises(ValidationError, validate_ico, "werwr")

    def test_valid_ico(self):
        validate_ico(27074358)

    def test_valid_ico_as_string(self):
        validate_ico("27074358")

    def test_empty_ico(self):
        self.assertRaises(ValidationError, validate_ico, "")