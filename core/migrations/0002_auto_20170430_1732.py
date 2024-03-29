# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='deadline',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
