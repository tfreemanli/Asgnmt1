# Generated by Django 5.1.8 on 2025-04-22 08:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWRL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='check_in_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_out_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='TWRL.room'),
            preserve_default=False,
        ),
    ]
