from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Sum

from profiles.validators import AlphaNumericUnderscoreValidator


def validate_username(value):
    if not value.isalnum() and "_" not in value:
        raise ValidationError("Username must contain only letters, digits, and underscores!")


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(3), AlphaNumericUnderscoreValidator()],
        error_messages={
            'min_length': 'Username must be at least 3 chars long!',
        },
        null=False,
        blank=False,
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(21, "Age requirement: 21 years and above."),
        ],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    @staticmethod
    def get_last_profile():
        return Profile.objects.last()

    @property
    def cars_total(self):
        return self.car_set.aggregate(Sum('price', default=0))['price__sum']

