# Generated by Django 3.0.11 on 2020-11-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201124_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='numero',
        ),
        migrations.AddField(
            model_name='profile',
            name='numero',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]
