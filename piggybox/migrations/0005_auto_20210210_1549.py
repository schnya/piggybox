# Generated by Django 3.1.6 on 2021-02-10 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggybox', '0004_auto_20210210_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='in_out',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-999999), django.core.validators.MaxValueValidator(999999)], verbose_name='収支'),
        ),
    ]
