# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-19 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nagios_monitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduledevent',
            old_name='last_run',
            new_name='last_seen',
        ),
    ]