# Generated by Django 5.1.2 on 2024-10-26 06:56

import django.core.validators
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, help_text='Age requirement: 21 years and above.', null=True, validators=[django.core.validators.MinValueValidator(21, 'Age requirement: 21 years and above.')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(error_messages={'min_length': 'Username must be at least 3 chars long!'}, max_length=15, validators=[django.core.validators.MinLengthValidator(3), profiles.validators.AlphaNumericUnderscoreValidator()]),
        ),
    ]