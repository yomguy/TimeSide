# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0011_auto_20161004_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processor',
            name='pid',
            field=models.CharField(max_length=128, unique=True, verbose_name='pid'),
        ),
    ]