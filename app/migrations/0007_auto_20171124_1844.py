# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20171124_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Author'),
        ),
    ]
