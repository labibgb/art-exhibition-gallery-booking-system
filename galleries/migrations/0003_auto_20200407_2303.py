# Generated by Django 3.0.5 on 2020-04-07 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='galleries.Location'),
        ),
    ]
