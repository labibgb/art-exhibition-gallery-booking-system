# Generated by Django 3.0.5 on 2020-04-11 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_auto_20200411_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
