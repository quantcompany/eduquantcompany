# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20161020_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='fa_icon',
            field=models.CharField(default='fa-graduation-cap', max_length=20),
        ),
    ]