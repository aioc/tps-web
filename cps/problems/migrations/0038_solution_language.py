# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-21 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0037_auto_20161119_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='language',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='language'),
        ),
    ]
