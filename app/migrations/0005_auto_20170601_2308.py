# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170601_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_num',
            field=models.CharField(max_length=45),
        ),
    ]
