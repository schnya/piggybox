# Generated by Django 3.1.6 on 2021-02-10 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggybox', '0006_schedule_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='status',
            new_name='category',
        ),
    ]
