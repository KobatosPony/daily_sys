# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-25 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winter_sakura', '0002_auto_20171224_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesetting',
            name='value',
            field=models.DateField(),
        ),
    ]
