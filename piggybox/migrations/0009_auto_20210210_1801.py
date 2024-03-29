# Generated by Django 3.1.6 on 2021-02-10 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('piggybox', '0008_auto_20210210_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='category',
            field=models.CharField(choices=[('poc', 'おこずかい'), ('sal', '給与'), ('foo', '食費'), ('boo', '教育'), ('tra', '交通費'), ('sho', 'ショッピング'), ('prs', 'プレゼント'), ('ent', '交際費'), ('fee', '手数料'), ('oth', 'その他')], default='foo', max_length=3, verbose_name='カテゴリー'),
        ),
    ]
