# Generated by Django 3.0.5 on 2020-04-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_infotable_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotable',
            name='active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
