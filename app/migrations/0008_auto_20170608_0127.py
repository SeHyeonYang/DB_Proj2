# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170607_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='end_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='section',
            name='start_time',
            field=models.IntegerField(),
        ),
    ]