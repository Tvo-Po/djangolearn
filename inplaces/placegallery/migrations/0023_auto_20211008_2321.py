# Generated by Django 3.2.6 on 2021-10-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placegallery', '0022_auto_20211008_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestingplace',
            name='cord_x',
            field=models.FloatField(blank=True, null=True, verbose_name='X coordinate'),
        ),
        migrations.AlterField(
            model_name='interestingplace',
            name='cord_y',
            field=models.FloatField(blank=True, null=True, verbose_name='Y coordinate'),
        ),
    ]