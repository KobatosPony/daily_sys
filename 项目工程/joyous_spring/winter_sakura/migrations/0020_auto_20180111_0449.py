# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-10 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0019_auto_20180111_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinfo',
            name='check_type',
        ),
        migrations.RemoveField(
            model_name='checkinfo',
            name='dept_id',
        ),
        migrations.RemoveField(
            model_name='checkinfo',
            name='staff_id',
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('0', '男'), ('1', '女')], max_length=20, verbose_name='性别'),
        ),
        migrations.DeleteModel(
            name='CheckInfo',
        ),
        migrations.DeleteModel(
            name='CheckType',
        ),
    ]
