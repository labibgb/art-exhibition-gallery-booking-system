# Generated by Django 3.0.5 on 2020-04-11 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20200411_1042'),
        ('galleries', '0005_auto_20200411_1042'),
        ('payment', '0005_auto_20200411_1042'),
        ('user', '0016_auto_20200411_0311'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
