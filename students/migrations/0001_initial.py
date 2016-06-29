# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentsprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='\u0406\u043c\u044f')),
                ('lastname', models.CharField(max_length=50, verbose_name='\u041f\u0440\u0438\u0437\u0432\u0456\u0449\u0435')),
                ('middlename', models.CharField(max_length=50, verbose_name='\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456')),
                ('date_of_birth', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('students_ticket', models.IntegerField(default=0, verbose_name='\u2116 \u0411\u0456\u043b\u0435\u0442\u0443')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametry.Groupofstudents', verbose_name='\u0413\u0440\u0443\u043f\u0430')),
            ],
        ),
    ]
