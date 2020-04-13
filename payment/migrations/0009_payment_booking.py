# Generated by Django 3.0.5 on 2020-04-13 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20200413_1220'),
        ('payment', '0008_remove_payment_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='booking',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.Booking'),
            preserve_default=False,
        ),
    ]
