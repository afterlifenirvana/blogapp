# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171117_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('tech', 'Technology'), ('misc', 'Miscellaneous')], default='tech', max_length=64),
        ),
    ]
