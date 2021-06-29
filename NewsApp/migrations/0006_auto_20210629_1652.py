# Generated by Django 2.0 on 2021-06-29 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_auto_20210629_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='NULL', max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Время публикации новости'),
        ),
    ]
