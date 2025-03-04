# Generated by Django 3.0.5 on 2020-04-13 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galleries', '0006_gallery_rent_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.Gallery'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
