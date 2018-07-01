# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 14:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=100)),
                ('min_participants', models.IntegerField(default=0)),
                ('max_participants', models.IntegerField(default=1)),
                ('team', models.CharField(choices=[('Single Team', 'SingleTeam'), ('Multiple Team', 'MultipleTeam')], max_length=15)),
            ],
            options={
                'ordering': ('sport_name',),
            },
        ),
        migrations.CreateModel(
            name='SportFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(blank=True, max_length=20)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sports.Sport')),
            ],
        ),
    ]
