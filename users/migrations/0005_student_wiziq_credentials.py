# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='wiziq_credentials',
            field=models.TextField(blank=True),
        ),
    ]
