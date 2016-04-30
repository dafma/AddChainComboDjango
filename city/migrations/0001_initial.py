# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-30 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, verbose_name='City Name')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='state.State')),
            ],
        ),
    ]
