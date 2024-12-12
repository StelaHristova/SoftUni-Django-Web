# Generated by Django 5.1.2 on 2024-10-14 20:46

import forumApp.posts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[forumApp.posts.validators.BadLanguageValidator()]),
        ),
    ]