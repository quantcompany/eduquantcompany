# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20161114_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='wiziq_credentials',
            field=models.TextField(blank=True, default='\n        <b>Email</b>: ######## <br>\n        <b>Password</b>: ########\n        '),
        ),
    ]
