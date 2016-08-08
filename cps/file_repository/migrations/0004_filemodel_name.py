# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import hashlib
import os


def set_file_name_as_name(apps, schema_editor):
    FileModel = apps.get_model("file_repository", "filemodel")
    db_alias = schema_editor.connection.alias
    for file_model in FileModel.objects.using(db_alias).all():
        if file_model.file.name:
            file_model.name = os.path.split(file_model.file.name)[1]
        else:
            file_model.name = hashlib.sha1(file_model.pk)
        file_model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('file_repository', '0003_delete_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='name',
            field=models.CharField(null=True, max_length=256, verbose_name='name'),
        ),
        migrations.RunPython(set_file_name_as_name, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='filemodel',
            name='name',
            field=models.CharField(null=False, max_length=256, verbose_name='name'),
        )

    ]
