# Generated by Django 2.0 on 2021-06-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0004_auto_20210629_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='csrf_token',
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.TextField(verbose_name='Время публикации новости'),
        ),
    ]