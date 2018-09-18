# Generated by Django 2.1.1 on 2018-09-18 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0010_player_league'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='league',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='fifa.League'),
        ),
        migrations.AlterField(
            model_name='player',
            name='record',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='fifa.Record'),
        ),
    ]
