# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20170809_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='answers',
            field=models.TextField(default=''),
        ),
    ]
