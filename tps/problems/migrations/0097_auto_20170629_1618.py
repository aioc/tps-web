# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-29 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_repository', '0007_filesystemmodel_gitbinaryfile_gitfile'),
        ('problems', '0096_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSystemPopulatedModel',
            fields=[
            ],
        ),
        migrations.CreateModel(
            name='JSONModel',
            fields=[
            ],
        ),
        migrations.CreateModel(
            name='ManuallyPopulatedModel',
            fields=[
            ],
        ),
        migrations.CreateModel(
            name='NewProblemBranch',
            fields=[
            ],
        ),
        migrations.CreateModel(
            name='RecursiveDirectoryModel',
            fields=[
            ],
        ),
        migrations.CreateModel(
            name='ResourceBase',
            fields=[
            ],
        ),
        migrations.CreateModel(
            name='ResourceFile',
            fields=[
            ],
            bases=('file_repository.gitfile',),
        ),
        migrations.CreateModel(
            name='SolutionFile',
            fields=[
            ],
            bases=('file_repository.gitfile',),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
            ],
            bases=('file_repository.gitfile',),
        ),
        migrations.CreateModel(
            name='StatementAttachment',
            fields=[
            ],
            bases=('file_repository.gitbinaryfile',),
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={},
        ),
        migrations.AlterModelOptions(
            name='subtask',
            options={},
        ),
        migrations.AlterModelOptions(
            name='testcase',
            options={},
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='checker',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='code_name',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='description',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='id',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='memory_limit',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='score_type',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='score_type_parameters',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='statement',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='task_type',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='task_type_parameters',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='time_limit',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='title',
        ),
        migrations.RemoveField(
            model_name='solutionrun',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='solutionrun',
            name='solutions',
        ),
        migrations.RemoveField(
            model_name='solutionrun',
            name='testcases',
        ),
        migrations.AddField(
            model_name='solutionrun',
            name='base_problem',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='problems.Problem', verbose_name='problem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solutionrun',
            name='commit_id',
            field=models.CharField(default='', max_length=256, verbose_name='commit id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='files',
            field=models.ManyToManyField(blank=True, to='file_repository.FileModel', verbose_name='problem files'),
        ),
        migrations.AlterField(
            model_name='problembranch',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='problems.Problem', verbose_name='problem'),
        ),
        migrations.AlterField(
            model_name='validatorresult',
            name='testcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validation_results', to='problems.ValidatorResult', verbose_name='testcase'),
        ),
        migrations.AlterField(
            model_name='validatorresult',
            name='validator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='problems.ValidatorResult', verbose_name='validator'),
        ),
        migrations.AlterUniqueTogether(
            name='checker',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='grader',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='inputgenerator',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='solution',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='solutionrunresult',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='solutionsubtaskexpectedverdict',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='subtask',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='validator',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='checker',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='grader',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='inputgenerator',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='resource',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='solution',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='subtask',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='testcase',
            index_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='validator',
            index_together=set([]),
        ),
        migrations.CreateModel(
            name='GraderFile',
            fields=[
            ],
            bases=('file_repository.gitfile', 'problems.recursivedirectorymodel'),
        ),
        migrations.CreateModel(
            name='ProblemCommit',
            fields=[
            ],
            bases=('problems.filesystempopulatedmodel',),
        ),
        migrations.CreateModel(
            name='SourceFile',
            fields=[
            ],
            bases=('problems.resourcebase',),
        ),
        migrations.RemoveField(
            model_name='checker',
            name='compilation_finished',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='compilation_task_id',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='compiled_file',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='file',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='id',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='last_compile_log',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='name',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='checker',
            name='source_language',
        ),
        migrations.RemoveField(
            model_name='grader',
            name='code',
        ),
        migrations.RemoveField(
            model_name='grader',
            name='id',
        ),
        migrations.RemoveField(
            model_name='grader',
            name='language',
        ),
        migrations.RemoveField(
            model_name='grader',
            name='name',
        ),
        migrations.RemoveField(
            model_name='grader',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='compilation_finished',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='compilation_task_id',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='compiled_file',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='file',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='id',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='is_enabled',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='last_compile_log',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='name',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='source_language',
        ),
        migrations.RemoveField(
            model_name='inputgenerator',
            name='text_data',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='file',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='id',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='name',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='code',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='id',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='language',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='name',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='verdict',
        ),
        migrations.RemoveField(
            model_name='solutionrunresult',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='solutionrunresult',
            name='testcase',
        ),
        migrations.RemoveField(
            model_name='solutionsubtaskexpectedverdict',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='solutionsubtaskexpectedverdict',
            name='subtask',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='score',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='testcases',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='_input_generated_file',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='_input_generation_parameters',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='_input_generator_name',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='_input_uploaded_file',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='_output_generated_file',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='_output_uploaded_file',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='generator',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='id',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='input_generation_log',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='input_generation_successful',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='input_generation_task_id',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='input_static',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='judge_initialization_message',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='judge_initialization_successful',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='judge_initialization_task_id',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='output_generation_log',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='output_generation_successful',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='output_generation_task_id',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='output_static',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='testcase_number',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='_subtasks',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='compilation_finished',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='compilation_task_id',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='compiled_file',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='file',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='global_validator',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='id',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='last_compile_log',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='name',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='validator',
            name='source_language',
        ),
    ]
