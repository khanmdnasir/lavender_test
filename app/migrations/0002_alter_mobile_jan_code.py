# Generated by Django 4.0 on 2021-12-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='jan_code',
            field=models.IntegerField(unique=True),
        ),
    ]
