# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180530_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='document_chefdepartement',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='document_pg',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='document_scolarite',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pv_cpc',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]