# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20171202_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='hours_worked',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
