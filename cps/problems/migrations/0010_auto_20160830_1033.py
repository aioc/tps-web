# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0009_auto_20160828_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemrevision',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='revision owner'),
        ),
        migrations.AlterField(
            model_name='sourcefile',
            name='_compiled_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='file_repository.FileModel', verbose_name='compiled file'),
        ),
    ]
