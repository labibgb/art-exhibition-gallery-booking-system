# Generated by Django 3.0.5 on 2020-04-10 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
