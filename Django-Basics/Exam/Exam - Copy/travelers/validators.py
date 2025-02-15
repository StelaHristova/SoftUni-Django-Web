from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaDigitValidator:

    def __init__(self, message=None):
        self.message = message or 'Your nickname is invalid!'

    def __call__(self, value):
        if not value.isalpha() and not value.isdigit():
            raise ValidationError(self.message)


@deconstructible
class CharValidator:

    def __init__(self, message=None):
        self.message = message

    def __call__(self, value):
        if len(value) != 3:
            raise ValidationError(self.message)