# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20161111_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='wiziq_credentials',
            field=models.TextField(blank=True, default='<p>\n        Para recibir tus clases, debes ingresar a <a href="http://quantcompany.wiziq.com/">http://quantcompany.wiziq.com/</a> con las siguientes credenciales:\n        <br/>\n        Usuario: ########\n        Password: ########\n        <br/>\n        </p>'),
        ),
    ]
