# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161025_1104'),
        ('courses', '0005_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('cancelled', 'Cancelled'), ('finished', 'Finished')], default='pending', max_length=10)),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_id', models.CharField(max_length=100, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='courses.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='users.Student')),
            ],
            options={
                'ordering': ['last_modified', 'enrollment_date'],
            },
        ),
    ]
