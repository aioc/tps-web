# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-04 18:02
from __future__ import unicode_literals

from django.db import migrations
import problems.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0098_auto_20170704_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionrunresult',
            name='solution',
            field=problems.models.fields.DBToGitForeignKey(choices=None, commit_id_field_name='commit_id', default=None, editable=False, problem_field_name='base_problem', to='problems.Solution', verbose_name='solution'),
        ),
        migrations.AddField(
            model_name='solutionrunresult',
            name='testcase',
            field=problems.models.fields.DBToGitForeignKey(choices=None, commit_id_field_name='commit_id', default=None, editable=False, problem_field_name='base_problem', to='problems.TestCase', verbose_name='testcase'),
        ),
    ]