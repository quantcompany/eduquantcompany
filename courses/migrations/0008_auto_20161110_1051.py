# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 16:51
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify


def generate_slugs(apps, schema_editor):
    Course = apps.get_model('courses', 'Course')
    for course in Course.objects.all():
        course.slug = slugify(course.name)
        course.save()

class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_private_text'),
    ]

    operations = [
        migrations.RunPython(generate_slugs),
    ]
