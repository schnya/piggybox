# Generated by Django 3.1.6 on 2021-02-10 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggybox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='start_time',
        ),
    ]
