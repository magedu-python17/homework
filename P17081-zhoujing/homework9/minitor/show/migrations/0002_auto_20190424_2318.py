# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk_state',
            name='disk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Disk'),
        ),
    ]