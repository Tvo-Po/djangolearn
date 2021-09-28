# Generated by Django 3.2.6 on 2021-09-28 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placegallery', '0010_auto_20210928_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='placegallery.region'),
            preserve_default=False,
        ),
    ]
