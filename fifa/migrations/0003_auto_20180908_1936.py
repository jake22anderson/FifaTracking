# Generated by Django 2.1.1 on 2018-09-09 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0002_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='player',
        ),
        migrations.AddField(
            model_name='league',
            name='league',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifa.League'),
        ),
    ]