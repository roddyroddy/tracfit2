# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-29 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0005_user_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank_amrap',
            field=models.IntegerField(default=0),
        ),
    ]