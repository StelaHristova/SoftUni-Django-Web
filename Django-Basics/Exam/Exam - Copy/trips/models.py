from django.core.validators import MinLengthValidator
from django.db import models


class Trip(models.Model):
    destination = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        validators=[
            MinLengthValidator(3),
        ]
    )

    summary = models.TextField(
        null=False,
        blank=False,
    )

    start_date = models.DateField(
        null=False,
        blank=False,
    )

    duration = models.PositiveSmallIntegerField(
        default=1,
        null=False,
        blank=False,
        help_text='*Duration in days is expected.',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    traveler = models.ForeignKey(
        to='travelers.Traveler',
        on_delete=models.CASCADE,
        editable=False,
        related_name='trips'
    )
