# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-31 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0077_auto_20170328_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merge',
            name='base_revision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='problems.ProblemRevision'),
        ),
    ]
