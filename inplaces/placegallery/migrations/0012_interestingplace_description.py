# Generated by Django 3.2.6 on 2021-10-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placegallery', '0011_auto_20210928_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='interestingplace',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]