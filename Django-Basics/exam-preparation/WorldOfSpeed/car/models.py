from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car.choices import TypeChoices


def validate_year(value):
    if value < 1999 or value > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        blank=False,
        null=False,
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            validate_year
        ]
    )

    image_url = models.URLField(
        unique=True,
        help_text="https://...",
        error_messages={
            "unique": "This image URL is already in use! Provide a new one."
        }
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ]
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='cars',
        editable=False

    )
