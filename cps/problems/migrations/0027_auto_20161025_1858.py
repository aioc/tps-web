# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0026_auto_20161025_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemrevision',
            name='judge_code',
            field=models.CharField(editable=False, max_length=128, null=True, verbose_name='judge code'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='judge_code',
            field=models.CharField(editable=False, max_length=128, null=True, verbose_name='judge code'),
        ),
    ]
