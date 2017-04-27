# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-26 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0081_auto_20170407_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='subtask_scores',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='subtask_verdict',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='tests_scores',
        ),
        migrations.AlterField(
            model_name='checker',
            name='source_language',
            field=models.CharField(choices=[('c++', 'c++'), ('java', 'java'), ('pas', 'pas')], max_length=200),
        ),
        migrations.AlterField(
            model_name='inputgenerator',
            name='source_language',
            field=models.CharField(choices=[('c++', 'c++'), ('java', 'java'), ('pas', 'pas')], max_length=200),
        ),
        migrations.AlterField(
            model_name='solutionsubtaskexpectedscore',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask_scores', to='problems.Solution', verbose_name='solution'),
        ),
        migrations.AlterField(
            model_name='solutionsubtaskexpectedverdict',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask_verdict', to='problems.Solution', verbose_name='solution'),
        ),
        migrations.AlterField(
            model_name='solutiontestexpectedscore',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_scores', to='problems.Solution', verbose_name='solution'),
        ),
        migrations.AlterField(
            model_name='validator',
            name='source_language',
            field=models.CharField(choices=[('c++', 'c++'), ('java', 'java'), ('pas', 'pas')], max_length=200),
        ),
    ]