from django.core.validators import MinLengthValidator
from django.db import models

from travelers.validators import AlphaDigitValidator, CharValidator


class Traveler(models.Model):
    nickname = models.CharField(
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(3),
            AlphaDigitValidator(),
        ],
        help_text='*Nicknames can contain only letters and digits.',
        null=False,
        blank=False,
    )

    email = models.EmailField(
        unique=True,
        max_length=30,
        null=False,
        blank=False,
    )

    country = models.CharField(
        max_length=3,
        unique=True,
        null=False,
        blank=False,
        validators=[
            CharValidator(),
        ]
    )

    about_me = models.TextField(
        null=True,
        blank=True,
    )
