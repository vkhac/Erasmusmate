# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0003_auto_20170602_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatprofile',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
