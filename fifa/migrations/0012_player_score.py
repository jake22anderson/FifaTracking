# Generated by Django 2.1.1 on 2018-09-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0011_auto_20180918_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default='0'),
        ),
    ]
