# Generated by Django 3.2.6 on 2021-10-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placegallery', '0020_comment_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='interestingplace',
            name='is_checked',
            field=models.BooleanField(default=True),
        ),
    ]
