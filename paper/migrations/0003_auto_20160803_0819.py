# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_auto_20160803_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.Subject'),
        ),
    ]
