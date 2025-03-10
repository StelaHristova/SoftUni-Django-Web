from django.core.validators import MinLengthValidator
from django.db import models

from authors.validators import AlphaValidator, DigitValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            AlphaValidator(),
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            AlphaValidator(),
        ],
        null=False,
        blank=False,
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            DigitValidator(),
        ],
        help_text='Your passcode must be a combination of 6 digits',
        null=False,
        blank=False,
    )

    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )


