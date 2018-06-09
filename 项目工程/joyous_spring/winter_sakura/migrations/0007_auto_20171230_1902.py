# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-30 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0006_auto_20171226_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemsetting',
            options={'verbose_name': '系统设置'},
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(choices=[('1', '女'), ('0', '男')], max_length=4),
        ),
    ]
