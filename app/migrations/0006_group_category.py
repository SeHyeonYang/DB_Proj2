# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170601_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
            preserve_default=False,
        ),
    ]
