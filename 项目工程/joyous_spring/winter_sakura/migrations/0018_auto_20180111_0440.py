# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-01-10 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0017_auto_20180111_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='statu',
            new_name='state',
        ),
        migrations.AddField(
            model_name='staff',
            name='day_note',
            field=models.IntegerField(default=0, verbose_name='记录'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('0', '男'), ('1', '女')], max_length=20, verbose_name='性别'),
        ),
    ]
