# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notice', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('comments', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=80)),
                ('date', models.DateField(auto_now_add=True)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('times', models.IntegerField()),
                ('location', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('due_date', models.DateField()),
                ('max_capacity', models.IntegerField()),
                ('min_capacity', models.IntegerField()),
                ('cur_apply_num', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.IntegerField()),
                ('email_addr', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('nickname', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='teach',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher'),
        ),
        migrations.AddField(
            model_name='take',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='receiver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to='app.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='sender_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_id', to='app.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
