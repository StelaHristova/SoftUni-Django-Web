from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(5),
        ],
        unique=True,
        error_messages={
            'unique': 'Oops! That title is already taken. How about something fresh and fun?'
        },
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        help_text='Share your funniest furry photo URL!',
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        to='authors.Author',
        on_delete=models.CASCADE,
        editable=False,
        related_name='posts',
    )

    def __str__(self):
        return self.title