# Generated by Django 5.1.8 on 2025-04-24 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWRL', '0002_reservation_check_in_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='TWRL.room'),
        ),
    ]
