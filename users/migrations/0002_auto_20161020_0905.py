# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'instructor', 'verbose_name_plural': 'instructors'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
