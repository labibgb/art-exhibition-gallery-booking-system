# Generated by Django 3.0.5 on 2020-04-10 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_user'),
        ('payment', '0003_auto_20200411_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.User'),
        ),
    ]
