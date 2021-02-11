# Generated by Django 3.1.6 on 2021-02-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggybox', '0005_auto_20210210_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.CharField(blank=True, choices=[('poc', 'おこずかい'), ('sal', '給与'), ('foo', '食費'), ('boo', '教育'), ('tra', '交通費'), ('sho', 'ショッピング'), ('prs', 'プレゼント'), ('ent', '交際費'), ('fee', '手数料'), ('oth', 'その他')], default='foo', max_length=3),
        ),
    ]
