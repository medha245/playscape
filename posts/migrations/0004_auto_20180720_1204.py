# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180716_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='activity',
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
