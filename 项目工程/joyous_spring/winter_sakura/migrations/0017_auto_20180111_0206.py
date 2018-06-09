# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-10 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0016_auto_20180107_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='statu',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('1', '女'), ('0', '男')], max_length=20, verbose_name='性别'),
        ),
    ]
