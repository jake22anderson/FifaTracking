# Generated by Django 2.1.1 on 2018-09-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0009_auto_20180918_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifa.League'),
        ),
    ]
