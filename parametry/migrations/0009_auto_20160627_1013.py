# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametry', '0008_groupofstudents_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupofstudents',
            name='lead',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
        ),
    ]