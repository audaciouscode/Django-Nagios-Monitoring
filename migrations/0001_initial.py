# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-19 22:00

from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ScheduledEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=2048, unique=True)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('warning_minutes', models.IntegerField(default=5)),
                ('error_minutes', models.IntegerField(default=15)),
            ],
        ),
    ]
