# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180531_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document_scolarite',
            name='file',
            field=models.FileField(upload_to='document_scol/'),
        ),
    ]