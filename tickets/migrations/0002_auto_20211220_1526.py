# Generated by Django 3.2.10 on 2021-12-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.AlterField(
            model_name='guest',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]