# Generated by Django 5.1.1 on 2025-02-15 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_approve_posts', 'Can approve posts')]},
        ),
    ]
