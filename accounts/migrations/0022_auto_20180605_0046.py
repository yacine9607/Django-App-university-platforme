# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20180605_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commun',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.senders'),
        ),
    ]
