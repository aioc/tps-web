# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-10 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0087_auto_20170503_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemdata',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]
