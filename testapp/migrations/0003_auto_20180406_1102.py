# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-06 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_tabuser_pswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabmoney',
            name='time_sec',
            field=models.CharField(default=1522983347307, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tabmoney',
            name='time_str',
            field=models.CharField(default='2018-04-06 10:55:47', max_length=30),
            preserve_default=False,
        ),
    ]